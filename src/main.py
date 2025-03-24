from textnode import *
from extract_markdown import *
from copier import *
from generate import *
import sys

def main():
    explore_src("static", "docs", [])
    generate_pages_recursive()
    


main()