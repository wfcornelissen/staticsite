import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold","http")
        node2 = TextNode("This is a text node", "bold","http")
        self.assertEqual(node, node2)

    def test_eq_empty_text(self):
        node = TextNode("","bold","http")
        node2 = TextNode("","bold","http")
        self.assertEqual(node, node2)
    
    def test_eq_empty_type(self):
        node = TextNode("This is a text node", "","http")
        node2 = TextNode("This is a text node", "","http")
        self.assertEqual(node, node2)

    def test_eq_empty_url(self):
        node = TextNode("This is a text node", "bold","")
        node2 = TextNode("This is a text node", "bold","")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("a","bold","http")
        node2 = TextNode("This is a text node", "bold","http")
        self.assertNotEqual(node, node2)

    def test_not_equ_text(self):
        node = TextNode("This is a text node","bold","http")
        node2 = TextNode("a", "bold","http")
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", "bold","http")
        node2 = TextNode("This is a text node", "a","http")
        self.assertNotEqual(node, node2)
        
    def test_not_equ_type(self):
        node = TextNode("This is a text node", "a","http")
        node2 = TextNode("This is a text node", "bold","http")
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", "bold","http")
        node2 = TextNode("This is a text node", "bold","a")
        self.assertNotEqual(node, node2)
    
    def test_not_equ_type(self):
        node = TextNode("This is a text node", "bold","a")
        node2 = TextNode("This is a text node", "bold","http")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()