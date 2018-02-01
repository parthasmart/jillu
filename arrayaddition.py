
def main():
i=0 
arr=[]
n=int(input("enter a array size:"))
no=int(input("perform addition"))
print("enter number")
for i in range(0,n):
y=int(input())
arr.append(y)
a=0
no=int(input("perform addition"))
for i in range(0,no):
a+=arr[i]
print(a)
