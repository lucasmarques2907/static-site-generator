import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node_child = HTMLNode("b", "This is a bold text", None, None)
        node = HTMLNode("p", "This is a paragraph", [node_child], None)
        self.assertEqual(f'HTMLNode(p, This is a paragraph, [HTMLNode(b, This is a bold text, None, None)], None)', repr(node))

    def test_repr2(self):
        node = HTMLNode("a", "This is a link to a website", None, {"href":"https://www.python.org/", "target":"_blank"})
        self.assertEqual(f'HTMLNode(a, This is a link to a website, None, {"{'href': 'https://www.python.org/', 'target': '_blank'}"})', repr(node))

    def test_props_to_html(self):
        node = HTMLNode("a", "This is a link to a website", None, {"href":"https://www.python.org/", "target":"_blank"})
        self.assertEqual(f' href="https://www.python.org/" target="_blank"', node.props_to_html())
    
    def test_repr_none(self):
        node = HTMLNode()
        self.assertEqual(f'HTMLNode(None, None, None, None)', repr(node))
    
    def test_valus(self):
        node = HTMLNode("div", "This is a div")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "This is a div")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
if __name__ == "__main__":
    unittest.main()