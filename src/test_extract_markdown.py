import unittest
from extract_markdown import *

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot.dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [
            ("to boot.dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ])

    def test_extract_markdown_images(self):
        text = "This is text with an image ![alt text](https://www.boot.dev/image.png)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [
            ("alt text", "https://www.boot.dev/image.png")
        ])

    def test_extract_markdown_links_and_images(self):
        text = "This is text with a link [to boot.dev](https://www.boot.dev) and an image ![alt text](https://www.boot.dev/image.png)"
        links = extract_markdown_links(text)
        images = extract_markdown_images(text)
        self.assertEqual(links, [
            ("to boot.dev", "https://www.boot.dev")
        ])
        self.assertEqual(images, [
            ("alt text", "https://www.boot.dev/image.png")
        ])

if __name__ == "__main__":
    unittest.main()