# Empower two numbers without using the power symbol
Number_A,Number_B=[int(x)for x in input("Get Number A and B:").split(" ")]
while(Number_B>1):
    Number_A=Number_A*Number_A
    Number_B-=1
    
print(Number_A)