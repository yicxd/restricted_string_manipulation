initial_index = -1

word = input("Enter a word: ")
find = input("What word would you like to find: ") 


for letters in range(len(word)):
    if word[letters : letters + len(find)] == find:
        initial_index = letters
        break


if initial_index == -1:
    print("ValueError")
else:
    print(initial_index)