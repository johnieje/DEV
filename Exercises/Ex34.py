"""
Birthday Script: Writing to JSON file
"""
import json


# convert dictionary to JSON and save to file

def convert_json(dictionary, json_file):
    with open(json_file, 'w') as f:
        if json.dump(dictionary, f):
            return True


def convert_dict(json_file):
    with open(json_file, 'r') as f:
        dict_data = json.load(f)
        return dict_data


if __name__ == '__main__':

    # Ask for birthday
    user_input = input("Who's birthday do you want to look up? ")

    # Get birthdays List
    birthdays = convert_dict('birthday.json')

    # Check if user input is in the birthday List
    if user_input in birthdays:
        print(f"{user_input} birthday is {birthdays[user_input]}")
    else:
        print(f'No birthday record for {user_input}.')

        #  Add new entry to birthdays dictionary
        choice = input(f'Would you like to add {user_input} birthday to the list? (yes or no): ')

        # convert choice to lowercase
        choice = choice.lower()
        if choice == 'yes':
            birthday = input('Enter birthday (05/17/2020): ')

            # Add new entry in the dictionary
            birthdays[user_input] = birthday
            try:
                convert_json(birthdays, 'birthday.json')
                print('Added Successfully.')
            except ValueError as e:
                print('Failed')
        elif choice == 'no':
            print('Exiting...')
        else:
            raise Exception('Invalid Input')
