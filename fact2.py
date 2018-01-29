num=int(input("enter the number:"))
fact=1
if num<0:
print("enter the number:")
elif num==0:
print("the factorial of o is 1")
else:
for i in range(1,num+1):
fact=fact*i
print(fact)
