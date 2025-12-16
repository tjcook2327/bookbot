#Open a file and return the contents
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
#Use the contents of a book file and return the number of words in the file
def get_num_words(book_obj):
    words = len(book_obj.split())
    return words
#Iterate through list and return a dictionary of characters and  number times a character is in the file
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
#Sort a character dictionary by the number of times character is in dict most to least
def sort_on(items):
    return items
def sort_list(char_dict):
    char_list = []
    char_sorted_dict = {}
    for key, value in char_dict.items():
        char_list.append((value, key))
        char_list.sort(reverse=True, key=sort_on)
    for key2, value2 in char_list:
        if value2.isalpha() == True:
            char_sorted_dict.update({value2 : key2}) 
    return char_sorted_dict

        


