anything = input("Enter any thing: ")#can be just spaces
secword = input("Enter a word or sentence: ")
rjustnum = int(input("Enter a number for adjusting: "))

def rjust(origword, width): #will return the original plus spaces
    return " " * (width - len(origword)) + origword #switched places

firword =   rjust(anything, rjustnum)

print(firword, secword)