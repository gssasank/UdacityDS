cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()
    
#The range() function takes three integer arguments, the first and third of which are optional:
#range(start,stop,step)  ONly stop is compulsory
#The 'start' argument is the first number of the sequence. If unspecified, 'start' defaults to 0.
#The 'stop' argument is 1 more than the last number of the sequence. This argument must be specified.
#The 'step' argument is the difference between each number in the sequence. If unspecified, 'step' defaults to 1.
#Notes on using range():

#If you specify one integer inside the parentheses withrange(), it's used as the value for 'stop,' and the defaults are used for the other two.
#e.g. - range(4) returns 0, 1, 2, 3
#If you specify two integers inside the parentheses withrange(), they're used for 'start' and 'stop,' and the default is used for 'step.'
#e.g. - range(2, 6) returns 2, 3, 4, 5
#Or you can specify all three integers for 'start', 'stop', and 'step.'
#e.g. - range(1, 10, 2) returns 1, 3, 5, 7, 9