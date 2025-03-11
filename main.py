from stats import get_word_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    print_report(book_text)


def sort_on(item):
    return item[1]


def print_report(book_text):
    word_count = get_word_count(book_text)
    character_list = list(get_character_map(book_text).items())
    character_list.sort(key=sort_on, reverse=True)
    print(f"--- Begin report of {sys.argv[1]} ---")
    print(f"{word_count} words found in the document")
    print()
    for c in character_list:
        if c[0].isalpha():
            print(f"{c[0]}: {c[1]}")
    print("--- End report ---")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_character_map(s):
    result = {}
    for character in s.lower():
        if not character in result:
            result[character] = 1
        else:
            result[character] += 1
    return result


main()
