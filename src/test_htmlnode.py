import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    # HTML Node Tests
    def test_repr(self):
        node_child = HTMLNode("b", "This is a bold text", None, None)
        node = HTMLNode("p", "This is a paragraph", [node_child], None)
        self.assertEqual(f'HTMLNode(p, This is a paragraph, [HTMLNode(b, This is a bold text, None, None)], None)', repr(node))

    def test_repr2(self):
        node = HTMLNode("a", "This is a link to a website", None, {"href":"https://www.python.org", "target":"_blank"})
        self.assertEqual(f'HTMLNode(a, This is a link to a website, None, {"{'href': 'https://www.python.org', 'target': '_blank'}"})', repr(node))

    def test_props_to_html(self):
        node = HTMLNode("a", "This is a link to a website", None, {"href":"https://www.python.org", "target":"_blank"})
        self.assertEqual(f' href="https://www.python.org" target="_blank"', node.props_to_html())
    
    def test_repr_none(self):
        node = HTMLNode()
        self.assertEqual(f'HTMLNode(None, None, None, None)', repr(node))
    
    def test_values(self):
        node = HTMLNode("div", "This is a div")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "This is a div")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    # Leaf Node Tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Check out this cool website!", {"href":"https://www.boot.dev","target":"_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev" target="_blank">Check out this cool website!</a>')

    def test_leaf_To_html_no_tag(self):
            node = LeafNode(None, "Hello, world!")
            self.assertEqual(node.to_html(), "Hello, world!")

    # Parent Node Tests
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


if __name__ == "__main__":
    unittest.main()