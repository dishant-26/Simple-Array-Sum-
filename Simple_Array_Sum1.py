# make a list
list = []

# ask for how many numbers
num = int(input('How many numbers : '))

# loop to ask input for how many numabers
for n in range(num):
    numbers = int(input('Enter number :'))
    # to add a number in the list
    list.append(numbers)

# sum(list) to do the addtition of all the numbers in the list
a = sum(list)
print("Sum of elements in given list is :", a)
