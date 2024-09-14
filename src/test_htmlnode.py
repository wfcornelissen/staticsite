import unittest
from htmlnode import HTMLNode
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
        
        

if __name__ == "__main__":
    unittest.main()