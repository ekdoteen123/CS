def copy_even_lines(input_file, output_file="evenlines.txt"):
    try:
        with open(input_file, "r") as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return

    even_lines = [line.rstrip("\n") for index, line in enumerate(lines, start=1) if index % 2 == 0]

    with open(output_file, "w") as outfile:
        for line in even_lines:
            outfile.write(line + "\n")

    print("Contents of evenlines.txt:")
    for line in even_lines:
        print(line)
