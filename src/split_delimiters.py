from textnode import *
from htmlnode import *



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            pass
    return new_nodes

node = [TextNode("this is a textnode", TextType.CODE,"www.google.com")]
print(split_nodes_delimiter(node," ",TextType.CODE))