# R=0
# i=R
# name=input("enter the name")
# b=name
# while i<b:
#         K=R
#         while K<=R:
#             print(K,end=" ")
#             K=K+1
#             a=R
#             while a<=R:
#               print(a)
#               a=a+1
#             i=i+1


num=(input('enter the number'))
if num%3==0:
    print("choco")
elif num%7==0:
    print("late")
elif num%3==0 and num%7==0:
    print("cholcolate")
else:
    print("not")