from stats import get_num_words
from stats import get_char_count
import sys


def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read() 
        return file_contents

def main():
    book_path = sys.argv
    if len(book_path) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    text = get_book_text(book_path[1]).lower()
    num_words = get_num_words(text)
    char_dict = get_char_count(text)
    
    print(f"============ BOOKBOT ============ \n Analyzing book found at {book_path[1]}... \n")
    print(f"----------- Word Count ---------- \n Found {num_words} total words")
    print("--------- Character Count -------")
    for i in char_dict:
        print(f"{i[0]}: {i[1]}")
    print("============= END ===============")
    
main()

