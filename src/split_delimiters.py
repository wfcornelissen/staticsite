from src.textnode import *
from src.htmlnode import *
import re



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = [] #List to append nodes to
    delim_count = 0 #Used for delimiter count check
    #iterate over list
    for node in old_nodes:
        #check for non-text types and append them to new list
        if node.text_type is not TextType.TEXT:
            print("Fokweet")
            new_nodes.append(node)
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
            if segment.startswith(delimiter) and segment.endswith(delimiter):
                # Remove the delimiters and create a new node with the specified text_type
                content = segment[len(delimiter):-len(delimiter)]
                new_nodes.append(TextNode(content, text_type))
            else:
                # Create a new node with the default text type
                new_nodes.append(TextNode(segment, TextType.TEXT))

    return new_nodes