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
                if i.isalpha() == True:
                    if i in letters_dict:
                        letters_dict[i] += 1
                    else:
                        letters_dict[i] = 1
    sorted_dict = sorted([(value, key)
                          for(key,value) in letters_dict.items()],
                          reverse=True)  
    return sorted_dict

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count()} words found in the document")
    dict = letter_count()
    for i in range(0, len(dict)):
        print(f"The {dict[i][1]} character was found {dict[i][0]} times")
    print("---End report---")

main()