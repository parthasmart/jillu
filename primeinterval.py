low=int(input("enter the number:"))
hig=int(input("enter the number:"))
for num in range(low,hig+1):
  if num>1:
  for i in range(2,num):
  if(num%i)==0:
  break
  else:
  print(num)
  
