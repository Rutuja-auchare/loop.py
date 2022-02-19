result_str="";    
for row in range(0,9):    
    for column in range(0,9):     
        if (column == 1 or ((row == 0 or row == 4) and column > 1 and column < 6) or (column == 6 and row != 0 and row < 4) or (column == row - 1 and row > 3)):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str)
print()
for row in range(6):
    for col in range (5):
        if ((col==0 or col==3) and row!=5) or (row==5 and(col>0 and col<3 )):
            print("*",end="   ")
        else:
            print(end=" ")
    print()
print()
for row in range (7):
    for col in range (6):
        if col==4 or (row==0 and col!=4):
            print("*",end=" ")
        else:
            print(end=" ")
    print()
print()
for row in range(6):
    for col in range (5):
        if ((col==0 or col==3) and row!=5) or (row==5 and(col>0 and col<3 )):
            print("*",end="   ")
        else:
            print(end=" ")
    print()


	
