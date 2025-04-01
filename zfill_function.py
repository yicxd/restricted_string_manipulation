word = input("Enter anything: ")
zero = int(input("how many of zeroes to fill: "))

if zero > len(word):
    filledz = ("0" * (zero - len(word))) + word
else:
    filledz = word #if there are no zeros to fill

print(filledz)