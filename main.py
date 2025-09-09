from stats import get_num_words
from stats import get_num_chars


def main(relative_path):
    print(get_num_words(relative_path)
          )
    print(get_num_chars(relative_path))


main('books/frankenstein.txt')
