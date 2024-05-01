def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    word_number = 0
    for word in words:
        word_number += 1
    print(word_number)

main()