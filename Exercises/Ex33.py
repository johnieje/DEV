"""
Birthday Script
"""

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815'
}

print('Welcome to the birthday dictionary. We know the birthdays of:')
for name, birthday in birthdays.items():
    print(f'{name}')

user_input = input("Who's birthday do you want to look up? ")

if user_input in birthdays:
    print(f"{user_input} birthday is {birthdays[user_input]}")
