def reverse_string():
    string_to_be_reversed = "Hello World but Backwards!"
    print("This is your string reversed: ", string_to_be_reversed[::-1])
reverse_string()

def pig_latin_conversion(word_to_be_converted):
    vowels  = "aeiou"
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
