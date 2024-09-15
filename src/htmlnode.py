class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        #An HTMLNode without a tag will just render as raw text
        #An HTMLNode without a value will be assumed to have children
        #An HTMLNode without children will be assumed to have a value
        #An HTMLNode without props simply won't have any attributes
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}={self.props[prop]}'
        return props_html
        
    def __repr__(self):
        return f'HTMLNode({self.tag},{self.value},{self.children},{self.props})'
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == "" or self.value is None:
            raise ValueError("All LeafNodes must have a value")
        
        if self.tag is None:
            return str(self.value)
            
        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        
        return f'<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>'
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.value:
            raise ValueError("ParentNodes should not contain values")
        
        if self.tag == "" or self.tag is None:
            raise ValueError("ParentNodes must have tags")

        if self.children == "" or self.children is None:
            raise ValueError("ParentNodes must have children(LeafNodes)")
        
        html_string = ""
        for child in self.children:
            html_string += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>'
            