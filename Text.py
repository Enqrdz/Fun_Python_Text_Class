def pig_latin_conversion(word_to_be_converted):
    vowels  = "aeiouAEIOU"
    string_of_consonants = ""
    pig_latin_append = "way"
    counter = 0

    for letter in word_to_be_converted:
        #if letter is a vowel
        if(vowels.find(letter) != -1):
            word_to_be_converted += string_of_consonants + pig_latin_append
            print(word_to_be_converted[counter::])
            break
        else:
            string_of_consonants += letter
            pig_latin_append = "ay"
            counter += 1
pig_latin_conversion("Child")


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
