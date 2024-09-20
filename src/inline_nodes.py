from htmlnode import *
from textnode import *
import re

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_of_old_nodes = []
    new_list = []
    final_list = []
    list_of_old_nodes.extend(old_nodes)
    del_check = str()
    counter = 0
    for node in list_of_old_nodes:
        new_list.extend(re.split(rf"({re.escape(delimiter)})",node.text))
    print(new_list)
    for node in enumerate(new_list):
        print(node)
        if node[1] == delimiter:
            counter += 1
        if node[1] != delimiter and not is_even(counter) and node[1] != "":
            final_list.append(TextNode(node[1], text_type))
        if node[1] != delimiter and is_even(counter) and node[1] != "":
            final_list.append(TextNode(node[1], text_type_text))

    #final_list = list(map(lambda x: TextNode(x,text_type),new_list))
    for node in final_list:
        print(node)
                 

def is_even(n):
    return n % 2 == 0

nodes = [
    #TextNode("This is text with a normal words", text_type_text),
    TextNode("This is text with a `code block word", text_type_code)
    #TextNode("This is text with a **bolded phrase** in **the** middle", text_type_bold),
    #TextNode("This is text with a *italicized phrase* in the middle", text_type_italic)
]
split_nodes_delimiter(nodes, "`",text_type_code)