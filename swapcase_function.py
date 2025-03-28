word = input("Enter any word or sentence: ")

def swapcase(self):
    list = []
    for char in word:
        if char.islower():
            list.append(char.upper())
        elif char.isupper():
            list.append(char.lower())
        else:
            list.append(char)
    return "".join(list)

swapped = swapcase(word)

print(swapped)