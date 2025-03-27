word = input("Enter any word: ")

def lower(word_input):
    lowercased_word = ""
    for char in word_input: 
        if char >= "A" and char <= "Z":
            #each letter has a unicode and the ord function handles it
            lower_chars = chr(ord(char) + 32) #the difference of upper and lowercased characters is 32
            lowercased_word += lower_chars
        else:
            lowercased_word += char
    return lowercased_word


print(lower(word))