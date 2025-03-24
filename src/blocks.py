

def markdown_to_blocks(markdown):
    new_blocks = markdown.split("\n\n")
    final_blocks = []
    for block in new_blocks:
        if block == "":
            continue
        if "\n" in block:
            lines = []
            for line in block.split("\n"):
                if line.strip() != "":
                    lines.append(line.strip())
            if lines:
                final_blocks.append("\n".join(lines))
        else:
            final_blocks.append(block.strip())
        
    return final_blocks