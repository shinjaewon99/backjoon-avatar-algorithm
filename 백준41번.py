# 10768번


m = int(input())
n = int(input())
if m < 2:
    print("Before")    
elif m == 2:
    if n == 18: 
        print("Special")
    elif n > 18: 
        print("After")
    else: 
        print("Before")        
else: 
    print("After")