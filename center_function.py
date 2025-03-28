word = input("Enter any word or sentence: ")
centnum = int(input("Enter a number for centering: "))

def center(origword, width):
    spaces = width - len(origword)
    return (' ' * (spaces//2)) + origword + (' ' * (spaces//2))#spaces in between the original word

centered = center(word, centnum)

print(centered)