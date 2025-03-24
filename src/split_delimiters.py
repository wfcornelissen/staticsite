from textnode import *
from htmlnode import *
from extract_markdown import *
import re


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = [] #List to append nodes to
    delim_count = 0 #Used for delimiter count check
    #iterate over list
    for node in old_nodes:
        #check for non-text types and append them to new list
        if node.text_type is not TextType.TEXT:
            print("Fokweet")
            new_nodes.append(node)
            continue
        #Iterate through characters to check for uneven delimiters
        for char in node.text:
            if char == delimiter:
                delim_count += 1
        if delim_count%2 != 0:
            delim_count = 0
            raise Exception("Invalid Markdown syntax (uneven delimiters)")
        #With all checks passed, split text.
        split_text = re.split(rf"({re.escape(delimiter)}.*?{re.escape(delimiter)})", node.text)

        for segment in split_text:
            # Skip empty segments
            if not segment:
                continue
                
            if segment.startswith(delimiter) and segment.endswith(delimiter):
                # Remove the delimiters and create a new node with the specified text_type
                content = segment[len(delimiter):-len(delimiter)]
                new_nodes.append(TextNode(content, text_type))
            else:
                # Create a new node with the default text type
                new_nodes.append(TextNode(segment, TextType.TEXT))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINKS, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes