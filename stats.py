def get_num_words(relative_path):
    num_words = 0
    with open(relative_path, 'r') as file:
        text = file.read()
        words = text.split()
        num_words = len(words)

    print(f"{num_words} words found in the document")


def get_num_chars(relative_path):
    new_dict = {}
    with open(relative_path, 'r') as file:
        text = file.read()
        for char in text.lower():
            if char in new_dict:
                new_dict[char] += 1
            else:
                new_dict[char] = 1
    print(new_dict)

    return new_dict
