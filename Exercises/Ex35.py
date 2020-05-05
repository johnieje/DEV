"""
https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html
extract the months of all the birthdays
"""
import json
from collections import Counter

num_to_string = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


def convert_dict(json_file):
    with open(json_file, 'r') as f:
        dict_data = json.load(f)
        return dict_data


# load JSON file as dictionary
birthdays = convert_dict('birthday.json')

months = []

for name, date in birthdays.items():
    month = int(date.split("/")[0])
    months.append(num_to_string[month])

print(Counter(months))
