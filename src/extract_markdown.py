import re

# images
#r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

# regular links
#r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

def extract_markdown_images(text):
    pattern = "!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = "(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_headers(text):
    lines = text.split("\n")
    header = ""
    for line in lines:
        if line.startswith("# "):
            header = line.strip("#").strip()
    return header


