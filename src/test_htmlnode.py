import unittest
from htmlnode import *
from textnode import *


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )



class TestLeafNode(unittest.TestCase):
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

class TestTextNodeToHTML(unittest.TestCase):
    def test_text_node_to_html(self):
        text_node = TextNode("Hello, world!", TextType.NORMAL)
        self.assertEqual(text_node_to_html(text_node), "Hello, world!")

    def test_bold_text_node_to_html(self):
        text_node = TextNode("Hello, world!", TextType.BOLD)
        self.assertEqual(text_node_to_html(text_node), "<b>Hello, world!</b>")

    def test_italic_text_node_to_html(self):
        text_node = TextNode("Hello, world!", TextType.ITALIC)
        self.assertEqual(text_node_to_html(text_node), "<i>Hello, world!</i>")

    def test_code_text_node_to_html(self):
        text_node = TextNode("Hello, world!", TextType.CODE)
        self.assertEqual(text_node_to_html(text_node), "<code>Hello, world!</code>")

    def test_link_text_node_to_html(self):
        text_node = TextNode("Hello, world!", TextType.LINKS, "https://boot.dev")
        self.assertEqual(text_node_to_html(text_node), "<a href=\"https://boot.dev\">Hello, world!</a>")

    def test_image_text_node_to_html(self):
        text_node = TextNode("Hello, world!", TextType.IMAGES, "https://boot.dev")
        self.assertEqual(text_node_to_html(text_node), "<img src=\"https://boot.dev\" alt=\"Hello, world!\" />")

if __name__ == "__main__":
    unittest.main()