squares = [x**2 for x in range(9)]
print(squares)

#if we wanna use an if statement
squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)
#if we wanna use an if..else statement, it goes in the middle
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)

# QUESTIONS BASED ON THE CONCEPT

#Q1
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names =[name.split()[0].lower() for name in names]
print(first_names)

#Q2
multiples_3 = [num for num in range(3,63) if num%3 == 0]
print(len(multiples_3))

#Q3
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [key for key, value in scores.items() if value>=65]
print(passed)
