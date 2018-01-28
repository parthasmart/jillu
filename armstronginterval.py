low=int(input("enter the number:"))
hig=int(input("enter the number:"))
for num in range (low,hig+1):
order=len(str(num))
sum=0
temp=num
while temp>0:
digit=temp%10
sum+=dig**order
temp//=10

if(temp==num):
print(num)
