from textnode import *
from htmlnode import *
import re
from extract_markdown import *

#split_nodes_image takes TextNode and splits it into different TextNodes similar to split_node_delimiter
    #example:
#     node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT,)
#       new_nodes = split_nodes_link([node])
#       Below is result
#       [
#       TextNode("This is text with a link ", TextType.TEXT),
#       TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#       TextNode(" and ", TextType.TEXT),
#       TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
#       ]
    
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.type == TextType.TEXT:
            images = extract_markdown_images(node.text)
            if images:
                for image in images:
                    new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes