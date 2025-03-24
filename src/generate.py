import os
from extract_markdown import *
from blocks import *
import shutil

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    if os.path.exists(dest_path):
        os.remove(dest_path)

    contents = open(from_path, "r").read()
    template = open(template_path, "r").read()
    html_node = markdown_to_html_node(contents)
    html = html_node.to_html()
    extracted_title = extract_markdown_headers(contents)
    template = template.replace("{{ Title }}", extracted_title)
    template = template.replace("{{ Content }}", html)
    template = template.replace("href=\"/", f"href=\"{basepath}")
    template = template.replace("src=\"/", f"src=\"{basepath}")

    try:
        open(dest_path, "w").write(template)
    except Exception as e:
        os.makedirs(os.path.dirname(dest_path))
        open(dest_path, "w").write(template)

    pass

def generate_pages_recursive(src=None, basepath = "/"):
    if src == None:
        src = "content"
    dest = "docs"
    if not os.path.exists(dest):
        os.makedirs(dest)
    template = "template.html"

    for dir in os.listdir(src):
        if os.path.isfile(src + "/" + dir):
            generate_page(src + "/" + dir, template, src.replace("content", dest) + "/" + dir.replace(".md", ".html"), basepath)
        else:
            generate_pages_recursive(src + "/" + dir, basepath)
            
