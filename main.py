import sys
from stats import sorted_list1


def main(relative_path):
    return sorted_list1(relative_path)


if sys.argv and len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
