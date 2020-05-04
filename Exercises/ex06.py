"""
Palindrome Script
"""

print('Welcome to the Palindrome Script')

user_input = input('Enter String: ')

# compare entered string to its reverse
if user_input[:] == user_input[::-1]:
    print('this string is a palindrome')
else:
    print('this string is not a palindrome')
