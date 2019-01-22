def converting_to_pig_latin(text):
    vowels  = "aeiouAEIOU"
    string_of_consonants = ""
    pig_latin_append = "way"
    index_of_text = 0

    if(vowels.find(text.index(0)) != -1):
        pig_latin_append = "ay"

    for char in text:
        #if char is a vowel
        if(vowels.find(char) != -1):
            word_to_be_converted += string_of_consonants + pig_latin_append
            print(text[counter::])
            break
        else:
            string_of_consonants += char
            counter += 1
converting_to_pig_latin("Child")


def count_vowels_in_text(text):
    vowels = "aeiouAEIOU"
    counter = 0

    for letter in text:
        if(vowels.find(letter) != -1):
            counter += 1
    print ("There are %s vowels in: %s" %(counter,text))
count_vowels_in_text("The Quick Brown Fox Jumped Over The Lazy Dog")


def get_reverse_string(string_to_be_reversed):
    return string_to_be_reversed[::-1]
print(get_reverse_string("Hello World but Backwards!"))


def remove_spaces_in_string(string_to_modify):
    return string_to_modify.replace(" ", "")
print(remove_spaces_in_string("Hello World!"))


def check_if_palindrome(string_to_check):
    string_to_check = remove_spaces_in_string(string_to_check)
    if(string_to_check == get_reverse_string(string_to_check)):
        print("%s is a palindrome!" %(string_to_check))
    else:
        print("%s is not a palindrome!" %(string_to_check))
check_if_palindrome("race car")


def count_words_in_text(text):
    counter = 1;
    for char in text:
        if(char == " "):
            counter += 1
    print("There are %s words in: %s!" %(counter,text))
count_words_in_text("Hello darkness my old friend")
