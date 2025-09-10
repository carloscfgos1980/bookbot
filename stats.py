# count the amount of words
def get_num_words(relative_path):
    num_words = 0
    with open(relative_path, 'r') as file:
        text = file.read()
        words = text.split()
        num_words = len(words)

    return f" Found {num_words} total words"

# createa a dictionary with the amount of characters


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

# sort the list based on the number of characters


def sort_on(items):
    return items["num"]

# create a sorted list of dictionaries with the characters and their amount

# first version of the function


def sorted_list(relative_path):
    my_dict = get_num_chars(relative_path)
    my_list = []

    # convert the dictionary to a list of dictionaries
    for key, value in my_dict.items():
        new_dict = {"char": key, "num": value}
        my_list.append(new_dict)

    # sort the list based on the number of characters
    my_list.sort(key=sort_on, reverse=True)

    # create dictionaries with only alphabetical characters.
    # The key is the character and the value is the amount of characters
    new_list = []
    for dic in my_list:
        if dic["char"].isalpha():
            new_dict = {dic["char"]: dic["num"]}
            new_list.append(new_dict)

    print(get_num_words(relative_path))

    # print the sorted list
    for dic in new_list:
        for key, value in dic.items():
            print(f"- {key}: {value}")

# second version of the function


def sorted_list1(relative_path):
    my_dict = get_num_chars(relative_path)
    my_list = []

    # convert the dictionary to a list of dictionaries
    for key, value in my_dict.items():
        new_dict = {"char": key, "num": value}
        my_list.append(new_dict)

    # sort the list based on the number of characters
    my_list.sort(key=sort_on, reverse=True)

    # iterate the list of dictionaries and then iterate each dictionary
    # to get the characters and their amount
    print(get_num_words(relative_path))
    for dic in my_list:
        if dic["char"].isalpha():
            char = dic["char"]
            num = dic["num"]
            print(f"- {char}: {num}")
