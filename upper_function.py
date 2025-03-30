word = input("Enter any word: ")

def upper(word_input):
    uppercased_word = ""
    for char in word_input: 
        if char >= "a" and char <= "z":
            #each letter has a unicode and the ord function handles it
            upper_chars = chr(ord(char) - 32) #the difference of upper and lowercased characters is 32
            uppercased_word += upper_chars
        else:
            uppercased_word += char
    return uppercased_word


print(upper(word))