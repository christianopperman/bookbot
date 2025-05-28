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