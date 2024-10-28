import unittest
import re

from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

class TestExtractMarkdown(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = "Here is an image ![alt text](https://www.boot.dev) in markdown."
        expected = [("alt text", "https://www.boot.dev")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)

        text = "Multiple images ![first](https://first.url) and ![second](https://second.url)."
        expected = [("first", "https://first.url"), ("second", "https://second.url")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)

        text = "No images here."
        expected = []
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)

    def test_extract_markdown_links(self):
        text = "Here is a link [link text](https://www.boot.dev) in markdown."
        expected = [("link text", "https://www.boot.dev")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

        text = "Multiple links [first](https://first.url) and [second](https://second.url)."
        expected = [("first", "https://first.url"), ("second", "https://second.url")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

        text = "No links here."
        expected = []
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )




if __name__ == "__main__":
    unittest.main()
