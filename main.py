def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print(file_contents)

    # word_split = file_contents.split()
    # word_count = len(word_split)
    # print(word_count)

    char_count = {}
    lower_string = file_contents.lower()

    for char in lower_string:
        if char in char_count and char.isalpha():
            char_count[char] += 1
        elif char.isalpha():
            char_count[char] = 1
    print(char_count)
    return char_count


main()
