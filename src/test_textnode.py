import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("This is a second text node", TextType.BOLD)
        node2 = TextNode("This is a second text node", TextType.BOLD)
        self.assertEqual(node, node2)

        nodeurl = TextNode("This is a text node", TextType.BOLD, "url")
        nodeurl2 = TextNode("This is a text node", TextType.BOLD, "url")
        self.assertEqual(nodeurl, nodeurl2)

        nodeurl = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        nodeurl2 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertEqual(nodeurl, nodeurl2)

        nodetype = TextNode("This is a text node", TextType.ITALIC)
        nodetype2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(nodetype, nodetype2)

        nodetype = TextNode("This is a text node", TextType.CODE)
        nodetype2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(nodetype, nodetype2)

        

    def test_uneq(self):
        uneqnodeurl = TextNode("This is a text node", TextType.BOLD, "url")
        uneqnodeurl2 = TextNode("This is a text node", TextType.BOLD, "url2")
        self.assertNotEqual(uneqnodeurl, uneqnodeurl2)

        uneqnodetype = TextNode("This is a equal text node with unequal type", TextType.BOLD)
        uneqnodetype2 = TextNode("This is a equal text node with unequal type", TextType.ITALIC)
        self.assertNotEqual(uneqnodetype, uneqnodetype2)

        uneqnodetext = TextNode("This is a unequal text node", TextType.BOLD)
        uneqnodetext2 = TextNode("This is a unequal text node2", TextType.BOLD)
        self.assertNotEqual(uneqnodetext,uneqnodetext2)

        uneqnodetext = TextNode("This is a unequal text node", TextType.BOLD)
        uneqnodetext2 = TextNode("zzzz", TextType.BOLD)
        self.assertNotEqual(uneqnodetext,uneqnodetext2)

    def test_split_nodes_delimiter_starting_word_delimited(self):
        node = TextNode("This is a text node", TextType.TEXT)
        nodeexp = [TextNode("This is a text node", TextType.TEXT)]

        node = TextNode("'This' is a code node", TextType.CODE)
        nodeexp = [TextNode("This", TextType.CODE), TextNode(" is a code node", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], "'", TextType.CODE), nodeexp)
        
        node = TextNode("**This** is a bold node", TextType.BOLD)
        nodeexp = [TextNode("This", TextType.BOLD), TextNode(" is a bold node", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), nodeexp)

        node = TextNode("*This* is an italic node", TextType.ITALIC)
        nodeexp = [TextNode("This", TextType.ITALIC), TextNode(" is an italic node", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), nodeexp)

    def test_split_nodes_delimiter_middle_word_delimited(self):
        node = TextNode("This is a text node", TextType.TEXT)
        nodeexp = [TextNode("This is a text node", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], "'", TextType.CODE), nodeexp)

        node = TextNode("This is a 'code' node", TextType.CODE)
        nodeexp = [TextNode("This is a ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" node", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], "'", TextType.CODE), nodeexp)

        node = TextNode("This is a **bold** node", TextType.BOLD)
        nodeexp = [TextNode("This is a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" node", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), nodeexp)

        node = TextNode("This is a *italic* node", TextType.ITALIC)
        nodeexp = [TextNode("This is a ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" node", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), nodeexp)

    def test_split_nodes_delimiter_ending_word_delimited(self):
        node = TextNode("This is a text node", TextType.TEXT)
        nodeexp = [TextNode("This is a text node", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], "'", TextType.CODE), nodeexp)

        node = TextNode("This is a code 'node'", TextType.CODE)
        nodeexp = [TextNode("This is a code ", TextType.TEXT), TextNode("node", TextType.CODE)]
        self.assertEqual(split_nodes_delimiter([node], "'", TextType.CODE), nodeexp)

        node = TextNode("This is a bold **node**", TextType.BOLD)
        nodeexp = [TextNode("This is a bold ", TextType.TEXT), TextNode("node", TextType.BOLD)]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), nodeexp)

        node = TextNode("This is an italic *node*", TextType.ITALIC)
        nodeexp = [TextNode("This is an italic ", TextType.TEXT), TextNode("node", TextType.ITALIC)]
        self.assertEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), nodeexp)
    
    def test_split_nodes_multiple_delimiters(self):
        node = TextNode("This is a text node", TextType.TEXT)
        nodeexp = [TextNode("This is a text node", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], "'", TextType.CODE), nodeexp)

        node = TextNode("This 'is' a 'code' node", TextType.CODE)
        nodeexp = [TextNode("This ", TextType.TEXT), TextNode("is", TextType.CODE), TextNode(" a ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" node", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], "'", TextType.CODE), nodeexp)

        node = TextNode("This **is** a **bold** node", TextType.BOLD)
        nodeexp = [TextNode("This ", TextType.TEXT), TextNode("is", TextType.BOLD), TextNode(" a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" node", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), nodeexp)

        node = TextNode("This *is* an *italic* node", TextType.ITALIC)
        nodeexp = [TextNode("This ", TextType.TEXT), TextNode("is", TextType.ITALIC), TextNode(" an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" node", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), nodeexp)

    # def test_split_nodes_delimiter_multiple_nodes(self):
    #     list_of_nodes = [TextNode("This is a text node", TextType.TEXT), 
    #                      TextNode("This is a **bold** node", TextType.BOLD),
    #                      TextNode("This is an *italic* node*", TextType.ITALIC),
    #                      TextNode("This is a 'code' node", TextType.CODE)]
    #     nodeexp = [TextNode("This is a text node", TextType.TEXT),
    #                 TextNode("This is a **bold** node", TextType.BOLD),
    #                 TextNode("This is a ", TextType.TEXT),TextNode("italic", TextType.ITALIC),TextNode(" node", TextType.TEXT),
    #                 TextNode("This is a 'code' node", TextType.CODE)]
    #     self.assertEqual(split_nodes_delimiter(list_of_nodes, "*", TextType.ITALIC), nodeexp)



if __name__ == "__main__":
    unittest.main()