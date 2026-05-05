import string


def normalize(word):
    return word.strip(string.punctuation)


def find_word_occurrences(filename, search_word):
    search_word = search_word.lower()
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return

    found_any = False
    for index, line in enumerate(lines, start=1):
        tokens = [normalize(token).lower() for token in line.split() if normalize(token)]
        occurrences = tokens.count(search_word)
        if occurrences:
            found_any = True
            label = "occurrence" if occurrences == 1 else "occurrences"
            print(f"Line {index}: {occurrences} {label}")

    if not found_any:
        print(f"The word '{search_word}' was not found.")
