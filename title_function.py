#same concept as capitalize except of cutting each letter splits->
#it insteads splits each word then does the capitalizes it

words = input("Enter any word or sentence: ")

def title(sentence):
    titled = []
    for word in sentence.split():#splits each word
        if word:#check if word is not empty
            titled_word = word.capitalize()#capitalizes the first letter
            titled.append(titled_word)
    return ' '.join(titled)


titled = title(words)
print(titled)