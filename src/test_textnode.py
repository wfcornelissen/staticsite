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

    


if __name__ == "__main__":
    unittest.main()