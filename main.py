from stats import get_word_count
from stats import num_of_chars
from stats import report

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    # Get the book in one string
    book = get_book_text(book_path)
    # Get and print word count
    word_count = get_word_count(book)
    # Get and print character count
    chars_dict = num_of_chars(book)
    sorted = report(chars_dict)
    print_report(book_path, word_count, sorted)

def print_report(book_path, word_count, sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in sorted:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")
    return


main()