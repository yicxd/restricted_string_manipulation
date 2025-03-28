word = input("Enter any word or sentence: ")

def swapcase(self):
    for char in word:
        if char >= "a" and char <= "z":
            char.upper()
        if char >= "A" and char <= "Z":
            char.lower()

swapped = swapcase(word)

print(swapped)