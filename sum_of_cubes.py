#problem-1
#sum of the cubes from n to m
m=int(input("Enter m value:"))
n=int(input("Enter n value:"))
total=0
if m>n:
    print("zero")
for i in range (m,n+1):
    total=total+i**3
print("Total:",total)
