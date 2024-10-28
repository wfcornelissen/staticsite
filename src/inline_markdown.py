from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = re.split(r"(!\[([^\[\]]*)\]\(([^\(\)]*)\))", old_node.text)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 4 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            elif i % 4 == 1:
                split_nodes.append(TextNode(sections[i+1], TextType.IMAGE, sections[i+2]))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = re.split(r"(\[([^\[\]]*)\]\(([^\(\)]*)\))", old_node.text)
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 4 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            elif i % 4 == 1:
                split_nodes.append(TextNode(sections[i+1], TextType.LINK, sections[i+2]))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    old_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_image(old_nodes)
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, '**', TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, '*', TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, '`', TextType.CODE)
    return new_nodes