# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!
 <stats.py>
# 1. get the amount of words
function: get_num_words
- read the document
- splits the words
- count the words using len()

# 2. Create a dictionary with the characters and the amount
- creeate empty dictioary
- read the file
- loop the string and convert to lower case
- add key(character) and values(amount) to the dictionary
- return the dictionary

# 3. sort the dictionary
- Just copy this function and call it later


# 4. Sorted List

- convert the dictionary to a list of dictionaries
- sort the list based on the number of characters
- create dictionaries with only alphabetical characters. The key is the character and the value is the amount of characters
- print the sorted list


<main.py>
import sys
from stats import sorted_list

def main(relative_path):
    return sorted_list(relative_path)

if sys.argv and len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])

Notes:
1.  I had a bug coz I was not returning sorted_list but print it so I print the right result but I got a wrong answer

2. <sys> built function allows me to pass argument when I run the program from the terminal

3. I made a second version of the function that sort list of dictionary and print em in the required format coz I realized In the first version I didn't quite grasp the dictinaries concepts and I made extra unneeded steps