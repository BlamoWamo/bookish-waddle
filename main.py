from stats import get_word_count, get_char_count
import sys

def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()       

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    text = get_book_text(book_path)

    # word count
    print("----------- Word Count ----------")
    word_count = get_word_count(text)
    print(f"Found {word_count} total words")

    # character count
    print("--------- Character Count -------")
    char_counts = get_char_count(text)
    for char, count in char_counts.items():
        print(f"{char}: {count}")

    print("============= END ===============")

main()
