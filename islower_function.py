word = input("Enter any word: ")

def islower(word_input):
    yep_lower = False #assumes its false first
    for char in word_input: 
        if char >= "a" and char <= "z":
            yep_lower = True
        if char >= "A" and char <= "Z":
            return False
    return yep_lower

print(islower(word))