#problem-6
#find and push the empty packets in the chocolate factory to the conveyer belt
array=[]
n=int(input("Enter the no of element:"))
for i in range (n):
    element=int(input("Enter the element for the array:"))
    array.append(element)
print("Array:",array)
empty=[]
arr1=[]
for j in array:
    if j==0:
        empty.append(j)
    else:
        arr1.append(j)
arr_sort=sorted(arr1)
final_output=arr_sort+empty
print("pushed empty packets to conveyer belt:",final_output)
