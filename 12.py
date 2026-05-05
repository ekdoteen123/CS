import os

INPUT_FILE = "Address.TXT"
OUTPUT_FILE = "NAdd.TXT"


def replace_delhi_in_file(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Input file not found: {input_path}")
        return

    with open(input_path, "r") as infile:
        content = infile.read()

    updated = content.replace("Delhi", "New Delhi")

    with open(output_path, "w") as outfile:
        outfile.write(updated)

    print(f"Replaced 'Delhi' with 'New Delhi' and wrote output to {output_path}.")
