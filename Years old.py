a,b,c=[int(i) for i in input("  enter born date:").split("/")]
d,e,f,j,k=[int(i) for i in input("  enter todays date:").split("/")]
g=d-a # for-up-item_year
h=e-b # for-up-item_Moon
i=f-c # for-up-item_hour
z=(g*365*24*60*60)+(h*30*24*60*60)+(i*24*60*60)+(j*3600)+(k*60)
print("Your Age In Second Is:",z)