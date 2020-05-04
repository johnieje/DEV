"""
Python script that takes a number and prints all the divisors
"""

print("A grogram for Divisors:")

# Enter the number
user_input = int(input('Enter Number: '))
num_list = []
while user_input > 0:
    for number in list(range(1, user_input)):
        if user_input % number == 0:
            num_list.append(number)
    break
print(num_list)
