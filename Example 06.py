Number=int(input("Get Number:"))
Counter=0
if(Number==0):
    Counter+=1
while(Number>0):
    if(Number%10==0):
        Counter+=1
    Number=Number//10
print("Tedad Sefr:",Counter)