def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print_report(book_path, book_text)


def sort_on(item):
    return item[1]


def print_report(book_path, book_text):
    word_count = get_word_count(book_text)
    character_list = list(get_character_map(book_text).items())
    character_list.sort(key=sort_on, reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in document")
    for c in character_list:
        if c[0].isalpha():
            print(f"The {c[0]} character was found {c[1]} times")
    print("--- End report ---")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_word_count(s):
    return len(s.split())


def get_character_map(s):
    result = {}
    for character in s.lower():
        if not character in result:
            result[character] = 1
        else:
            result[character] += 1
    return result


main()
