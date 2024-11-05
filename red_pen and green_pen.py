#problem-4
#red pen and green pen
list=[1,2,1,2,3,2,5]
count=0
for i in range(1,len(list)):
    if list[i]%2!=0:
        count=count+1
print("Swapped from green pen to red pen:",count)
