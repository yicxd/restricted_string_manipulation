word = input("Enter any thing: ")#can be just spaces
secword = input("Enter a second word: ")
ljustnum = int(input("Enter a number for adjusting: "))

def ljust(origword, width): #will return the original plus spaces
    return origword + " " * (width - len(origword))#spaces is equal to the width minus the length of the original

firword =   ljust(word, ljustnum)

print(firword, secword)