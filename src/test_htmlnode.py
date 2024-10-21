import unittest

from htmlnode import *

#self.tag = tag (pah1)
#self.value = value (string)
#self.children = children (list of HTMLNode objects)
#self.props = props (dictionary of key:value paris repping attributes)


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        tag1 = "h1"
        tag2 = "h2"
        tag3 = ""
        value1 = "This is a test string"
        value2 = "This is a second test string"
        value3 = ""
        props1 = {"href":"https://www.google.com"}
        props2 = {"href":"https://boot.dev"}
        props3 = {}
        child3 = []
        child2 = [HTMLNode(tag2,value2, child3, props2)]
        child1 = [HTMLNode(tag1,value1,child3,props1)]

        node1 = child1[0]
        node2 = child1[0]
        self.assertEqual(node1,node2)

        node1 = HTMLNode(tag1, value1, child1, props1)
        node2 = HTMLNode(tag1, value1, child1, props1)
        self.assertEqual(node1,node2)

        node1 = HTMLNode(tag2, value2, child2, props2)
        node2 = HTMLNode(tag2, value2, child2, props2)
        self.assertEqual(node1,node2)

        node1 = HTMLNode(tag3, value3, child3, props3)
        node2 = HTMLNode(tag3, value3, child3, props3)
        self.assertEqual(node1,node2)

    def test_uneq(self):
        tag1 = "h1"
        tag2 = "h2"
        value1 = "This is a test string"
        value2 = "This is a second test string"
        props1 = {"href": "https://www.google.com"}
        props2 = {"href": "https://boot.dev"}
        child1 = [HTMLNode(tag1, value1, [], props1)]
        child2 = [HTMLNode(tag2, value2, [], props2)]
    
        node1 = HTMLNode(tag1, value1, child1, props1)
        node2 = HTMLNode(tag2, value2, child2, props2)
        self.assertNotEqual(node1, node2)
    
        node1 = HTMLNode(tag1, value1, child1, props1)
        node2 = HTMLNode(tag1, value2, child1, props1)
        self.assertNotEqual(node1, node2)
    
        node1 = HTMLNode(tag1, value1, child1, props1)
        node2 = HTMLNode(tag1, value1, child2, props1)
        self.assertNotEqual(node1, node2)
    
        node1 = HTMLNode(tag1, value1, child1, props1)
        node2 = HTMLNode(tag1, value1, child1, props2)
        self.assertNotEqual(node1, node2)

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        tag = "p"
        value = "This is a paragraph."
        props = {"class": "text"}
        node = LeafNode(tag, value, props)
        expected_html = '<p class="text">This is a paragraph.</p>'
        self.assertEqual(node.to_html(), expected_html)

        node_no_props = LeafNode(tag, value)
        expected_html_no_props = '<p>This is a paragraph.</p>'
        self.assertEqual(node_no_props.to_html(), expected_html_no_props)

        node_no_tag = LeafNode(None, value)
        self.assertEqual(node_no_tag.to_html(), value)

    def test_to_html_no_value(self):
        tag = "p"
        with self.assertRaises(ValueError):
            node = LeafNode(tag, None)

    def test_eq(self):
        tag = "p"
        value = "This is a paragraph."
        props = {"class": "text"}
        node1 = LeafNode(tag, value, props)
        node2 = LeafNode(tag, value, props)
        self.assertEqual(node1, node2)

        node3 = LeafNode(tag, value)
        self.assertNotEqual(node1, node3)
        
class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        tag = "div"
        child_tag = "p"
        child_value = "This is a paragraph."
        child_props = {"class": "text"}
        child_node = LeafNode(child_tag, child_value, child_props)
        parent_node = ParentNode(tag, [child_node])
        expected_html = '<div><p class="text">This is a paragraph.</p></div>'
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_to_html_no_tag(self):
        child_tag = "p"
        child_value = "This is a paragraph."
        child_props = {"class": "text"}
        child_node = LeafNode(child_tag, child_value, child_props)
        with self.assertRaises(ValueError):
            parent_node = ParentNode(None, [child_node])
            parent_node.to_html()


    def test_to_html_no_children(self):
        tag = "div"
        with self.assertRaises(ValueError):
            parent_node = ParentNode(tag, [])
            parent_node.to_html()
        

    def test_eq(self):
        tag = "div"
        child_tag = "p"
        child_value = "This is a paragraph."
        child_props = {"class": "text"}
        child_node1 = LeafNode(child_tag, child_value, child_props)
        child_node2 = LeafNode(child_tag, child_value, child_props)
        parent_node1 = ParentNode(tag, [child_node1])
        parent_node2 = ParentNode(tag, [child_node2])
        self.assertEqual(parent_node1, parent_node2)

        parent_node3 = ParentNode(tag, [])
        self.assertNotEqual(parent_node1, parent_node3)

if __name__ == "__main__":
    unittest.main()