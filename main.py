import sys
from stats import get_number_of_words, get_number_of_characters, sort_chars


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + filepath)

    book_text = get_book_text(filepath)
    num_words = get_number_of_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    num_characters = get_number_of_characters(book_text)
    char_list = sort_chars(num_characters)
    print("--------- Character Count -------")
    for ch in char_list:
        if not ch["char"].isalpha():
            continue
        print(f"{ch['char']}: {ch['num']}")

    print("============= END ===============")


main()
