# definition
def amir(name):
    if name == 'amir':
        return "Yes is amir"
    else:
        print("name is't is",name)

x = amir('Jack')
print(x)

# part 02
def z(a, b=[]):
    b.append(a)
    return b

y=z(1)
y=z(3)
y=z(8)
print(y)

# more about arrays
fruits = ['Orange', 'Apple', 'Banana', 'Kiwi']
del fruits [2:4]
print(fruits)

# Tuple
ff = (1, 2, 3, 4)
for f in ff:
    print(f)

#  sets
G= {1, 3, 4, 5, 6, 7}
print(G)
if 8 not in G:
    print("8 isn't")
#  Part 02
G2=set('Jack')
print(G2)

# Json
ages = {'Jack':24, 'Mark':34, 'Kevin':89}
ages['amir']=20
print(ages)
print(ages['Mark'])
for (k, v) in ages.items():
    print(k, v)
# part02
names2 =['Jack','Kevin']
ages2 =[23, 60]
for n, a in zip(names2, ages2):
    print('\n\t', n, a)
# part03
p=['Mac', 'Win']
for i, j in enumerate(p):
    print(i, j)

# sort and reverse
l = [4, 5, 2, 3, 1, 9, 0]
print(sorted(l))
# Part02
for i in reversed(range(0,5)):
    print('\t',i)