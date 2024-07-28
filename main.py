def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    word_count = count_words(text)
    char_map = count_characters(text)
    char_list = map_to_list(char_map)

    print("Begin report of books/fkanenstein.txt")
    print(f"{word_count} words found in the document")
    for map in char_list:
        key = map["char"]
        value = map["count"]
        print(f"The {key} character was found {value} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())
  
def count_characters(text):
    char_map = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    return char_map

def map_to_list(char_map):
    list = [{"char": key, "count": value} for key, value in char_map.items()]
    list.sort(key=lambda x: x["char"])
    return list
main()