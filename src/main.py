from textnode import *
from extract_markdown import *
from copier import *
from generate import *

def main():
    explore_src("static", "public", [])
    generate_pages_recursive()


main()