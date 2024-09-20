import unittest
from htmlnode import *
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

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("p", [LeafNode("h1", "This is the test string", {"href":"https://boot.dev","class":"greeting"})])
        self.assertEqual(node.to_html(), "<p><h1 href=https://boot.dev class=greeting>This is the test string</h1></p>")

    def test_to_html_mult_children(self):
        node = ParentNode(
            "p", 
            [
                LeafNode("h1", "This is the test string 1", {"href 1":"https://boot.dev","class1":"greeting 1"}),
                LeafNode("h2", "This is the test string 2", {"href 2":"https://boot.dev"}),
                LeafNode("h3", "This is the test string 3", {"href 3":"https://boot.dev"})
            ]
        )
        self.assertEqual(node.to_html(), "<p><h1 href 1=https://boot.dev class1=greeting 1>This is the test string 1</h1><h2 href 2=https://boot.dev>This is the test string 2</h2><h3 href 3=https://boot.dev>This is the test string 3</h3></p>")

    def test_to_html_no_child(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError) as e:
            node.to_html()
        self.assertEqual(str(e.exception), "ParentNodes must have children(LeafNodes)")

    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("h1", "This is the test string", {"href":"https://boot.dev","class":"greeting"})])
        with self.assertRaises(ValueError) as e:
            node.to_html()
        self.assertEqual(str(e.exception), "ParentNodes must have tags")


if __name__ == "__main__":
    unittest.main()