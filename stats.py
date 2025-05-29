def get_word_count(book):
    words = book.split()
    return len(words)

def num_of_chars(book):
    book = book.lower()
    char_dict = {}
    for char in book:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict

def report(char_dict):
    sorted = []
    char_dict = char_dict.items()
    # Add a dictionary to each index of the list 
    for char, num in char_dict:
        dict = {"char": char, "num": num}
        sorted.append(dict)

    def sort_key_function(dict):
        return dict["num"]
    sorted.sort(reverse=True, key = sort_key_function)
    return sorted
    
