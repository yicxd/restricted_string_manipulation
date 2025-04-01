count = 0

word = input("Enter a word: ")
wordcount = input("Enter what to count: ") 


for letters in word:
    if letters == wordcount:
        count += 1


print(count)