import string


def normalize(word):
    return word.strip(string.punctuation)


def count_word_lengths(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return

    words = [normalize(token) for token in text.split() if normalize(token)]
    total = len(words)
    short = sum(1 for word in words if len(word) <= 3)
    long = sum(1 for word in words if len(word) > 3)

    print(f"Total words: {total}")
    print(f"Words of length <= 3: {short}")
    print(f"Words of length > 3: {long}")
