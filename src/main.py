from textnode import *
from extract_markdown import *
def main():
    link_text = "This is text with a link [to boot.dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    link_nodes = extract_markdown_links(link_text)
    print(link_nodes)
main()