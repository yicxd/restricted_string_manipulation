word = input("Enter any word or sentence: ")
chosen = input("What suffix would you like to remove: ")

def removesuffix(word, chosen):
    if word.endswith(chosen): #is now endswith
     return(word[:-len(chosen)])#negative starts from the end
    else:
       return word


print(removesuffix(word, chosen))