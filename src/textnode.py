from enum import Enum
from htmlnode import LeafNode, HTMLNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
            )
    
    #text, bold, italic, code, link, image
def text_node_to_html_node(text_node):
    
    class TextType(Enum):
        text = "text"
        bold = "bold"
        italic = "italic"
        code = "code"
        link = "link"
        image = "image"

    match text_node.text_type:
        case (TextType.text.value):
            return LeafNode(None, text_node.text).to_html()
        case (TextType.bold.value):
            return LeafNode("b", text_node.text).to_html()
        case (TextType.italic.value):
            return LeafNode("i", text_node.text).to_html()
        case (TextType.code.value):
            return LeafNode("code", text_node.text).to_html()
        case (TextType.link.value):
            return LeafNode("a", text_node.text, {"href":text_node.url}).to_html()
        case (TextType.image.value):
            return LeafNode("img",text_node.text,text_node.url).to_html()
        case _:
            raise Exception("No text type given")
        

def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"