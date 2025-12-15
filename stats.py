def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
def get_num_words(book_obj):
    words = len(book_obj.split())
    return words
    
def char_num_times(book_obj):
    char_list = {}
    for char in book_obj:
        if char == char.upper():
            char = char.lower()
        if char in char_list:
            
            char_list[char] += 1
        else:
            char_list[char] = 1
    return char_list