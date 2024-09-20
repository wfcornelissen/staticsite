from htmlnode import *
from textnode import *
import re

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    pairs = ()
    new_list = []
    final_list = []
    delim_count = 0

    #split TextNodes into tuples and make a list of tuples.
    for node in old_nodes:
        pairs = node.text, node.text_type
        new_list.append(pairs)

    #now iterate over strings to check for any invalid inputs.
    for node in new_list:
        if delimiter == " ":
            final_list.append(node)
        else:

            #Count amount of delimiters to check for any open-ended delimiters. Adjust to even count to use count in a maxsplit arguement.
            delim_count = node[0].count(delimiter)
            if not is_even(node[0].count(delimiter)):
                delim_count -= 1
                print(f"delim count after adjustment: {delim_count}")
            else:
                print(f"No delim adjustment needed: {delim_count}")

            #Split node into a new list for use to create new textnodes.
            new_list = list(enumerate(node[0].split(delimiter, delim_count)))

            #check index of node to determine text type. Index+1 = even is text, odds are type
            for node in new_list:
                if not is_even(node[0]+1):
                    final_list.append(TextNode(node[1],text_type_text))
                else:
                    final_list.append(TextNode(node[1],text_type))

    print(final_list)


def is_even(n):
    return n % 2 == 0

nodes = [
    TextNode("This is text with a normal words", text_type_text),
    TextNode("This is text with a `code block` and another `code block` phrase  with `open-ended delimiter", text_type_code),
    TextNode("This is text with a **bolded phrase** in the middle", text_type_bold),
    TextNode("This is text with a *italicized phrase* in the middle", text_type_italic)
]
split_nodes_delimiter(nodes, "*",text_type_code)