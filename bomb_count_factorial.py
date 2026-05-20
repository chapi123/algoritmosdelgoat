def factorial(n):
    print(n)
    if n == 0 :
        print("bomboclat")
        return 0
    else:
        return n* factorial(n-1)
    
#
#       factorial(4)
#       ├─ factorial(3)    
#       |   ├─factorial(2)
#       |   |  ├─factorial(1) 
#       |   |  |  ├─factorial(0) = 0 caso base
#
#
#
#
#