def get_num_words(relative_path):
    num_words = 0
    with open(relative_path, 'r') as file:
        text = file.read()
        words = text.split()
        num_words = len(words)

    return f" Found {num_words} total words"


def get_num_chars(relative_path):
    new_dict = {}
    with open(relative_path, 'r') as file:
        text = file.read()
        for char in text.lower():
            if char in new_dict:
                new_dict[char] += 1
            else:
                new_dict[char] = 1
    return new_dict


def sort_on(items):
    return items["num"]


def sorted_list(relative_path):
    my_dict = get_num_chars(relative_path)
    my_list = []

    for key, value in my_dict.items():
        new_dict = {"char": key, "num": value}
        my_list.append(new_dict)

    my_list.sort(key=sort_on, reverse=True)

    new_list = []
    for dic in my_list:
        if dic["char"].isalpha():
            new_dict = {dic["char"]: dic["num"]}
            new_list.append(new_dict)

    print(get_num_words(relative_path))
    for dic in new_list:
        for key, value in dic.items():
            print(f"- {key}: {value}")
