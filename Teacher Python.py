    #PART 1 = use print
print("PART 1:")
print("       HelloWorld")
    #PART 2 = use if and elif and else
print("PART 2:")
x=5
if x==3:
    print("       3")
elif x==4:
    print("       4")
else:
    print("       5")
    #PART 3 = use while and break
print("PART 3:")
x=9
while x==9:
    print("      ",x)
    break
    #PART 4 = use for and in
print("PART 4:")
x=[1,2,3,4]
for z in x:
    print("      ",z)
    #PART 5 = use continue
print("PART 5:")
x = 5
while x:
    x -= 1 
    if x % 2 != 0:
        continue 
    print("      ",x)
    #PART 6 = use def and range and return
print("PART 6:")
def F(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else :
    return F(n-1)+F(n-2)
for i in range(0,5):
  print ("      ",F(i))
    #PART 7 = use int and input and split and and and input and output
print("PART 7:")
a,b,c=[int(i) for i in input("       enter number:").split(" ")]
if a==2 and b==2 and c==2 :
    print("\n       yes all is 2")
print("\n               I love You Programming")  