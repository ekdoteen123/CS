import string


def normalize(word):
    return word.strip(string.punctuation)


def words_from_file(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return set()

    words = set()
    for token in text.split():
        cleaned = normalize(token).lower()
        if cleaned:
            words.add(cleaned)
    return words


def main():
    file1 = input("Enter the first filename: ").strip()
    file2 = input("Enter the second filename: ").strip()

    words1 = words_from_file(file1)
    words2 = words_from_file(file2)

    if not words1 or not words2:
        return

    common = sorted(words1.intersection(words2))
    print("Common words:")
    for word in common:
        print(word)
