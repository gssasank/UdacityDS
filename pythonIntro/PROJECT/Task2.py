"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


dct = dict()

for lst in calls:

    if lst[0] not in dct:
        dct[lst[0]] = int(lst[-1])
    else:
        dct[lst[0]] += int(lst[-1])

    if lst[1] not in dct:
        dct[lst[1]] = int(lst[-1])
    else :
        dct[lst[1]] += int(lst[-1])

maximum = 0
key = None
for key, value in dct.items():
    if value > maximum:
        maximum = value
        blip = key

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(blip, maximum))






