def print_multipel(char, count):
    for i in range(count):
        print(char, end='')

number = int(input("pls enter number:"))

max_line = number if number % 2 == 1 else number + 1
space_count = (number//2)
star_count = 1

for i in range(max_line):
    print_multipel(' ', space_count)
    print_multipel('*', star_count)
    print('')
    if i < max_line//2: 
        space_count += -1
        star_count += 2
    else:
        space_count += 1
        star_count += -2