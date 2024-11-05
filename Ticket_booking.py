#problem-2
#Ticket Booking
n=int(input("Enter the quantity:"))
total=0
for i in range(n):
    age=int(input("Enter age:"))
    if age<12:
        total=total+20
    elif age>60:
        total=total+30
    else:
        total=total+50
print(total)
