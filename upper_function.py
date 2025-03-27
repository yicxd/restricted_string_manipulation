word = input("Enter any word: ")

def isupper(word_input):
    yep_upper = False #assumes its false first
    for char in word_input: 
        if char >= "a" and char <= "z":
            return False
        if char >= "A" and char <= "Z":
            yep_upper = True
    return yep_upper

print(isupper(word))