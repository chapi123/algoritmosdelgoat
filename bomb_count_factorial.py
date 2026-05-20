def factorial(n):
    print(n)
    if n == 0 :
        print("bomboclat")
        return 0
    else:
        return n* factorial(n-1)
    
factorial(20)