def leapyear(n):
    if(n%4==0 and n%100!=0) or (n % 400==0):
        return True
    else:
        return False
    
n = int(input("Give the year to check leap year or not"))
if leapyear(n):
    print("{} is a leap year".format(n))
else:
    print("{} is not a leap year".format(n))
