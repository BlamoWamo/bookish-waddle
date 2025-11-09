from stats import get_word_count, get_char_count

def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()       

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    
    text = get_book_text()

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
