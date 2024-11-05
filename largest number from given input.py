#problem-5
#finding the largest number from the given number
n=int(input("Give the number:"))
str1=str(n)
lst=list(str1)
larger_value=sorted(lst,reverse=True)
str2="".join(larger_value)
Greater_number=int(str2)
print("Largest number from the given digit:",Greater_number)
