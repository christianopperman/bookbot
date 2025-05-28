from stats import count_words, count_characters


def read_book(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents


def gen_report(filepath):
    book = read_book(filepath)
    num_words = count_words(book)
    char_count = count_characters(book)
    print(f"--- Begin report of {filepath} ---")
    print(f"{num_words} words found in the document")
    for char, count in char_count.items():
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")


if __name__ == "__main__":
    path = 'books/frankenstein.txt'
    gen_report(path)
