word = input("Enter any word: ")

def isupper(word_input):
    for char in word_input: 
        if char >= 'A' and char <= 'Z':
            return True
        else:
            return False

print(isupper(word))