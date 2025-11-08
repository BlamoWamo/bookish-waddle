from stats import get_word_count, get_char_count

def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents        

def main():
    text = get_book_text()
    count = get_word_count(text)
    print(f"Found {count} total words")
    get_char_count(text)
    
main()
