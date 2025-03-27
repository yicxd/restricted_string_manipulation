word = input("Enter any word or sentence: ")
chosen = input("What prefix would you like to remove: ")

def removeprefix(word, chosen):
    if word.startswith(chosen):
     return(word[len(chosen): ]) #will return the word with the length of the prefix sliced
    else:
       return word


print(removeprefix(word, chosen))