word = []

def lstrip():
    for char in word:
        if char.isspace():#if its a space it will remove that character and will continue the loop
            word.remove(char)
            continue
        else: #if its anything else it will break
            break
