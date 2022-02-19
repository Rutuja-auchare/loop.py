i=int(input("enter the number to check armstrong"))
org=153
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if org==sum:
    print("number is armstrong")
else: 
    print("number is not armstrong")