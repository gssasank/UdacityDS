"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

market = set()

for lst in calls:
    if lst[0].startswith("140"):
        market.add(lst[0])

probable_market = set()

line1 = []
line2 = []
for l in calls:
    line1.append(l[0])
    line2.append(l[1])

for i in line1:
    if i not in line2:
        probable_market.add(i)

print(probable_market)

final = []

final = list(market) + list(probable_market)

print("These numbers could be telemarketers: \n{}".format('\n'.join(sorted(final))))
