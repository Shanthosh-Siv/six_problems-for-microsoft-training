#problem-3
#Food ordering
dic={"pizza":200,"burger":180,"Briyani":250,"Dosa":80,"Idly":50}
print("Available dish:",dic)
n=int(input("Enter n value:"))
total=0
for i in range(n):
    item=str(input("Enter your order:"))
    if item=="pizza":
        total=total+200
    elif item=="burger":
        total=total+180
    elif item=="Briyani":
        total=total+250
    elif item=="Dosa":
        total=total+80
    elif item=="Idly":
        total=total+50
    else:
        print("The item is not available")
if total>500:
    total1=total*(10/100)
    Grand_total=total-total1
    print("Grand total:",Grand_total)
else:
    print("Total:",total)
