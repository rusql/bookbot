def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(get_word_count(book_text))
    print (get_character_count(book_text))

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def get_word_count(s):
    return len(s.split())

def get_character_count(s):
    result = {}
    for character in s.lower():
        if not character in result:
            result[character] = 1
        else:
            result[character] +=1
    return result

main()
