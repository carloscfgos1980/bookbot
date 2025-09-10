import sys
from stats import sorted_list


def main(relative_path):
    if not relative_path:
        print("No file path provided.")
        sys.exit(1)
    return sorted_list(relative_path)


# 'books/frankenstein.txt'
if sys.argv and len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
