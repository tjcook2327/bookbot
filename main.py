from stats import get_book_text, get_num_words, char_num_times, sort_list

def main():
    book = get_book_text("books/frankenstein.txt")
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    print(f"Found {get_num_words(book)} total words")
    num_chars = char_num_times(book)
    print("--------- Character Count -------")

    sorted_list = sort_list(num_chars)
    for key, value in sorted_list.items():
        print(f"{key}: {value}")
    print("============= END ===============")
    
main()