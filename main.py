from stats import get_book_text, get_num_words, char_num_times

def main():
    book = get_book_text("books/frankenstein.txt")
    print(f"Found {get_num_words(book)} total words")
    num_chars = char_num_times(book)
    print(num_chars)

main()