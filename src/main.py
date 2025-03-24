from textnode import *
from extract_markdown import *
from copier import *
from generate import *
import sys

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print(f"Basepath: {basepath}")
    explore_src("static", "docs", [])
    generate_pages_recursive(basepath=basepath)
    


main()