#Variables
x1 = 20
x2 = 20.4 
x3 = 'Jack'
print('\n',type(x1),'\n',type(x2),'\n',type(x3))

#Note 01
# PascalCase = HowAreYou
# CamelCase = howAreYou
# Snake_Case = how_are_you

#Note 02
a = 49.9    
print('\n\t', round(a))

#   more about print
print("""
Hello
    World
        2021
""")

# Strings
word1 = 'Python'
print('\t', word1[1:4])
word2 = 'J' + word1[1:]
print('\t', word2)
print('\t', len(word1))

# Booleans
x = False
if (x):
    print(x) # Dont Print

print(5>1) #Output is True
print(1>5) #Output is False

# Arrays in Python
array01 = [1, 2, 3, 4]
array02 = ['Hello', 'Jack']
print(array01 + array02)
array01[0] = 6
print(array01)
array01.append(2*4)
print(array01)
print(array01[1:-2])

# While Loop
x = 0 
while x<10:
    print(x, end=' | ')
    x = x+1
print('Done')

# if elif else
x = 10
if x < 10:
    print('smaller than ten')
elif x ==10:
    print('equal to ten')
else:
    print('greater than ten')

# For Loop
name = ['Newyork', 'Amir', 'Ali', 'Hassan']
for esm in name:
    if len(esm) > 4:
        print(esm, '=is more than 4 character')
    else:
        print(esm)

#Break and Continue and Pass
# part1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numbers:
    if i == 5:
        continue # or break
    print(i)

# part2
for i in names:
    pass

#Range
# part1
for i in range(-10, -100, -10):
    print(i)

# part2
print( list(range(5)))