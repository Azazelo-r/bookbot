def main():
    path = "books/frankenstein.txt"
    print(f"--- Begin report of {path} ---")
    print(f"{get_total_words(get_book_text(path))} words found in the document\n")
    for k, v in sorted(
        get_total_characters(get_book_text(path)).items(), key=lambda x: -x[1]
    ):
        print(f"The {k!r} character was found {v} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_total_words(text):
    return len(text.split())


def get_total_characters(text):
    res = {}
    for c in text.lower():
        if c.isalpha():
            res[c] = res.get(c, 0) + 1
    return res


main()
