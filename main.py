with open("books/frankenstein.txt") as f:
        file_contents = f.read()

def word_count():
    words = file_contents.split()
    word_number = 0
    for word in words:
        word_number += 1
    return word_number

def letter_count():
    words = file_contents.split()
    letters_dict = {}
    for word in words:
        letters = word.split()
        for letter in letters:
            letter.split()
            for l in letter:
                i = l.lower()
                if i in letters_dict:
                    letters_dict[i] += 1
                else:
                    letters_dict[i] = 1
    return letters_dict


def main():
    print(word_count())
    print(letter_count())

main()