import unittest
from split_delimiters import *
from textnode import *
from htmlnode import *


class TestSplitDelimiters(unittest.TestCase):
    def test_split_delimiters(self):
        nodes = [
            TextNode("This is a text node", TextType.TEXT),
            TextNode("This is a text node", TextType.TEXT),
            TextNode("This is a text node", TextType.TEXT),
            TextNode("This is a text node", TextType.TEXT),
            TextNode("This is a text node", TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "|", TextType.TEXT)
        self.assertEqual(result, [
            TextNode("This is a text node", TextType.TEXT),
            TextNode("This is a text node", TextType.TEXT),
            TextNode("This is a text node", TextType.TEXT),
            TextNode("This is a text node", TextType.TEXT),
            TextNode("This is a text node", TextType.TEXT),
        ])

    def test_split_delimiters_italics(self):
        nodes = [
            TextNode("This is an _italic_ text node", TextType.TEXT),
            TextNode("This is a second _italic_ text node", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(result, [
            TextNode("This is an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text node", TextType.TEXT),
            TextNode("This is a second ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text node", TextType.TEXT),
        ])
        
    def test_split_delimiters_bold(self):
        nodes = [
            TextNode("This is a **bold** text node", TextType.TEXT),
            TextNode("This is a second **bold** text node", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text node", TextType.TEXT),
            TextNode("This is a second ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text node", TextType.TEXT),
        ])
    
    def test_split_delimiters_code(self):
        nodes = [
            TextNode("This is a `code` text node", TextType.TEXT),
            TextNode("This is a second `code` text node", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text node", TextType.TEXT),
            TextNode("This is a second ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text node", TextType.TEXT),
        ])

    def test_wrong_delim_passed(self):
        nodes = [
            TextNode("This is a **bold** text node", TextType.TEXT),
            TextNode("This is a second **bold** text node", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "[", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("This is a **bold** text node", TextType.TEXT),
            TextNode("This is a second **bold** text node", TextType.TEXT)
        ])

    def test_two_delimited_words(self):
        nodes = [
            TextNode("This is a **bold** text **node**", TextType.TEXT),
            TextNode("This is a second **bold** text **node**", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text ", TextType.TEXT),
            TextNode("node", TextType.BOLD),
            TextNode("This is a second ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text ", TextType.TEXT),
            TextNode("node", TextType.BOLD),
            
        ])

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINKS, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINKS, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINKS, "https://boot.dev"),
            ],
            nodes,
        )




if __name__ == "__main__":
    unittest.main()