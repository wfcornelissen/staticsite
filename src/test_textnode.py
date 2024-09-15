import unittest

from textnode import TextNode,text_node_to_html_node


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

    #text, bold, italic, code, link, image
    def test_txt_to_html_node(self):
        nodetext = TextNode("This is a text node", "text","https://boot.dev")
        nodebold = TextNode("This is a text node", "bold","https://boot.dev")
        nodeitalic = TextNode("This is a text node", "italic","https://boot.dev")
        nodecode = TextNode("This is a text node", "code","https://boot.dev")
        nodelink = TextNode("This is a text node", "link","https://boot.dev")
        nodeimage = TextNode("This is a text node", "image",{"href":"https://boot.dev"})

        self.assertEqual(text_node_to_html_node(nodetext), "This is a text node")
        self.assertEqual(text_node_to_html_node(nodebold), "<b>This is a text node</b>")
        self.assertEqual(text_node_to_html_node(nodeitalic), "<i>This is a text node</i>")
        self.assertEqual(text_node_to_html_node(nodecode), "<code>This is a text node</code>")
        self.assertEqual(text_node_to_html_node(nodelink), "<a href=https://boot.dev>This is a text node</a>")
        self.assertEqual(text_node_to_html_node(nodeimage), "<img href=https://boot.dev>This is a text node</img>")











if __name__ == "__main__":
    unittest.main()