import string

VOWELS = set("aeiouAEIOU")


def split_token(token):
    prefix = ""
    suffix = ""
    start = 0
    end = len(token)

    while start < end and not token[start].isalnum():
        prefix += token[start]
        start += 1

    while end > start and not token[end - 1].isalnum():
        suffix = token[end - 1] + suffix
        end -= 1

    core = token[start:end]
    return prefix, core, suffix


def transform_word(token):
    prefix, core, suffix = split_token(token)
    if not core:
        return token

    if core[0] in VOWELS:
        transformed = core[::-1]
    else:
        transformed = core.upper()

    return prefix + transformed + suffix


def count_long_words(tokens):
    count = 0
    for token in tokens:
        _, core, _ = split_token(token)
        if len(core) > 5:
            count += 1
    return count


def process_file(input_file, output_file="file2.txt"):
    try:
        with open(input_file, "r") as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return

    transformed_lines = []
    total_long = 0

    for line in lines:
        tokens = line.split()
        transformed_tokens = [transform_word(token) for token in tokens]
        transformed_lines.append(" ".join(transformed_tokens))
        total_long += count_long_words(tokens)

    with open(output_file, "w") as outfile:
        for line in transformed_lines:
            outfile.write(line + "\n")

    print("The contents of file2.txt should be:")
    for line in transformed_lines:
        print(line)
    print(f"Number of words with length greater than 5: {total_long}")
