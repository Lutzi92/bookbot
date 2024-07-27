def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = counting_words(text)
    print(f"--- Report on {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    printing_chars(counting_characters(text))
    print("--- end of report ---")

def counting_words(book):
    return len(book.split())
        
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def counting_characters(text):
    characters = {}
    text = text.lower()
    for char in text:
        if not characters.get(char) and char.isalpha():
            characters[char] = 0
        if char.isalpha():
            characters[char] +=1
    return characters

def printing_chars(dict):
    dict = sorting_dict(dict)
    for char in dict:
        print(f"The '{char.get('name')}' was found {char.get('num')} times")

def sort_on(dict):
    return dict["num"]

def sorting_dict(dict):
    sorted_list=[]
    for char in dict:
        sorted_list.append({"name":char, "num":dict.get(char)})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()