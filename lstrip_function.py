word = input("Enter any word or numbers with leading spaces: ")

def lstrip(char):
    i = 0
    #will count each char until its not a space
    while i < len(char) and char[i] == " ":
        i += 1
    #will slice away all the spaces
    return char[i:]

print(lstrip(word))
