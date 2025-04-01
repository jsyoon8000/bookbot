from stats import count_chars,count_words
import sys

def get_book_text(content):
    print(content)

if len(sys.argv) !=2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

book_path = sys.argv[1]

#./books/frankenstein.txt
with open(book_path) as book:
    book_contents = book.read()
    count_chars(book_contents)
