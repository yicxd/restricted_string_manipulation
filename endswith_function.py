word = input("Enter any word or sentence: ")
chosen = input("What would you like to check: ")

def endswith(ogword, end):
    #negative numbers in slicing starts at the end
    return ogword[-len(end):] == end


print(endswith(word, chosen))