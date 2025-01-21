def read_book(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    character_dict = {}
    for char in text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

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
