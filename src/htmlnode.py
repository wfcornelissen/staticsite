from textnode import TextType

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("No value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag")
        if self.children is None:
            raise ValueError("No children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
def text_node_to_html(text_node):
    if text_node.text_type == TextType.TEXT:
        return text_node.text
    elif text_node.text_type == TextType.BOLD:
        return f"<b>{text_node.text}</b>"
    elif text_node.text_type == TextType.ITALIC:
        return f"<i>{text_node.text}</i>"
    elif text_node.text_type == TextType.CODE:
        return f"<code>{text_node.text}</code>"
    elif text_node.text_type == TextType.LINKS:
        return f"<a href=\"{text_node.url}\">{text_node.text}</a>"
    elif text_node.text_type == TextType.IMAGE:
        return f"<img src=\"{text_node.url}\" alt=\"{text_node.text}\" />"
