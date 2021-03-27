import random
Number_a=0
Number_b=0
Number_c=0
while(Number_a!=6 and Number_b!=6 and Number_c!=6):
    Number_a=random.randint(1,6)
    Number_b=random.randint(1,6)
    Number_c=random.randint(1,6)
    print("\n","Tas1:",Number_a,"\n","Tas2:",Number_b,"\n","Tas3:",Number_c,"\n")
    if (Number_a==6 and Number_b==6 and Number_c==6):
        print("All is 6")
        break 