from stats import get_book_text, get_num_words, char_num_times, sort_list
import sys

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")

        print(f"Found {get_num_words(book)} total words")
        num_chars = char_num_times(book)
        print("--------- Character Count -------")

        sorted_list = sort_list(num_chars)
        for key, value in sorted_list.items():
            print(f"{key}: {value}")
        print("============= END ===============")


main()