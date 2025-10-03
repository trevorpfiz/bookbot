import sys

from stats import count_characters, count_words, sort_counts


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    character_counts = sort_counts(count_characters(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # Word Count
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")

    # Character Count
    print("--------- Character Count -------")
    for entry in character_counts:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
