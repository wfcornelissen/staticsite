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
        
    def __repr__(self) -> str:
        return f'HTMLNode({self.tag},{self.value},{self.children},{self.props})'