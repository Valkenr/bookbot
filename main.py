
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    char_dict = get_char_dictionary(text)
    sort_dict = sort_char_dictionary(char_dict)
    print_report(book_path, sort_dict)

def print_report(path, sort_dict):
    print(f"---Begin report of {path} ---")
    for i in range(0,len(sort_dict)):
        if sort_dict[i]['char'].isalpha():
            print(f"The '{sort_dict[i]['char']}' character was found {sort_dict[i]['num']} times")
    print(f"--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def get_char_dictionary(text):
    char_counts = {}
    for c in text:
        c_lower = c.lower()
        if c_lower in char_counts:
            char_counts[c_lower] += 1
        else:
            char_counts[c_lower] = 1
    return char_counts

def sort_char_dictionary(dict):
    char_list = []
    count = 0
    for d in dict:
        char_list.append({"char": d, "num": dict[d]})
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
            

main()
