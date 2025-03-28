word = input("Enter any word or sentence: ")#can be just spaces
secword = input("Enter a second word: ")

def ljust(origword, width): #will return the original plus spaces
    return origword + " " * (width - len(origword))#spaces is equal to the width minus the length of the original

firword =   ljust(word, 10)#width can be adjustable

print(firword, secword)