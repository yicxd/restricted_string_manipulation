word = input("Enter any word or sentence: ")
chosen = input("What would you like to check: ")

def startswith(ogword, start):
    #returns true if the start of the word is the same
    return ogword[ :len(start)] == start


print(startswith(word, chosen))

