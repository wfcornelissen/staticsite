import unittest
from textnode import *

print("Executing tests")

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "Wtf")
        node2 = TextNode("This is a text node", TextType.BOLD, "Wtf")
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text nod", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

    def test_different_types(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)

    def test_different_urls(self):
        node = TextNode("This is a text node", TextType.BOLD,"Wtf")
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)
    

if __name__ == "__main__":
    unittest.main()