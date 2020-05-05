"""
Birthday Histogram
"""
import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

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


def months_list(data_dict):
    months_of_year = []
    for x, y in data_dict.items():
        months_of_year.append(y)
    return months_of_year


# load JSON file as dictionary
birthdays = convert_dict('birthday.json')

months = []
output_file("graph.html")

for name, date in birthdays.items():
    month = int(date.split("/")[0])
    months.append(num_to_string[month])

# Assign the months to the X-Axis of the graph
my_month = months_list(num_to_string)

# Initialize counter
counter = 0

# Empty counter list for number of scientists with birthdays in a month
month_counter = []

# Special counter from Collections module
c = (Counter(months))
while counter < 12:
    for m in my_month:
        month_counter.append(c[my_month[counter]])
        counter += 1
# Assign month counter to Y-axis of graph
x = month_counter
y = my_month
print(x)
print(y)
p = figure()
p.vbar(x=x, top=y, width=0.5)
show(p)
