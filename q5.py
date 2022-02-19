counter=1
while counter<=100:
    if   counter%3==0:
            print("nav")
    elif counter%7==0:
            print("gurukul")
    elif counter%3==0 and counter%7==0:
            print("navgurukul")
    else:
            print(counter)
    counter=counter+1
    