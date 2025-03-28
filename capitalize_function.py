word = input("Enter any word or sentence: ")

def capitalize(origword):
    if not origword:#if its a decimal or anything else it will just return it
        return origword
    first_char = origword[0].upper() #removes the rest of the letters except first
    rest_chars = ''.join([c.lower() for c in origword[1:]])#lowers the rest
    return first_char + rest_chars #add the first and the rest of the characters

print(capitalize(word))