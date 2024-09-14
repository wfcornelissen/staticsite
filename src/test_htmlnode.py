import unittest
from htmlnode import HTMLNode, LeafNode
#An HTMLNode without a tag will just render as raw text
#An HTMLNode without a value will be assumed to have children
#An HTMLNode without children will be assumed to have a value
#An HTMLNode without props simply won't have any attributes


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("h1", "This is the test string", None, {"href":"https://boot.dev","class":"greeting"})
        self.assertEqual(node.props_to_html()," href=https://boot.dev class=greeting")
    
    def test_to_html2(self):
        node = HTMLNode("h1", "This is the test string", None, {"a":"b", "c":"d"})
        self.assertEqual(node.props_to_html()," a=b c=d")

    def test_values(self):
        node = HTMLNode("h1", "This is the test string", None, {"href":"https://boot.dev"})

        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "This is the test string")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props_to_html()," href=https://boot.dev")
        
        
class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("h1", "This is the test string",None)
        self.assertEqual(node.to_html(), "<h1>This is the test string</h1>")
    
    def test_to_html_with_prop(self):
        node = LeafNode("h1", "This is the test string", {"href":"https://boot.dev"})
        self.assertEqual(node.to_html(), "<h1 href=https://boot.dev>This is the test string</h1>")

if __name__ == "__main__":
    unittest.main()