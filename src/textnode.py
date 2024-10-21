import re
from enum import Enum


class TextType(Enum):
    TEXT = "text" 
    BOLD = "bold"#**
    ITALIC = "italic"#*
    CODE = "code"#'
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if text_type == TextType.TEXT or delimiter == " ":
            new_nodes.append(node)
        else:
            pass

        
    
    return new_nodes
                
