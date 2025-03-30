word = input("Enter any thing: ")#can be just spaces
secword = input("Enter a second word: ")
rjustnum = int(input("Enter a number for adjusting: "))

def rjust(origword, width): #will return the original plus spaces
    return " " * (width - len(origword)) + origword #spaces now go first

firword =   rjust(word, rjustnum)

print(firword, secword)