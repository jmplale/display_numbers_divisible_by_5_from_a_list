# write the list of the numbers
numbers = [10, 20, 33, 46,55]

# print the given sentences
print(f"Given list is {numbers}")
print("Divisible by 5")

# use a list
number_list = list(numbers)

# use a for loop
for divisible in number_list:
    # use an if statement
    if divisible % 5 == 0:
        print(divisible)