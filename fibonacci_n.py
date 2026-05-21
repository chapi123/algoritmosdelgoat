def fibonacci (n) :
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#
#                              F(5)
#                             /    \ 
#                            /      \ 
#                           /        \   
#                        F(4)       F(3)     
#                       /    \     /    \ 
#                      /      \  F(1)    F(2)
#                    F(3)     F(2)      /    \ 
#                   /   \     /   \   F(1)   F(0)
#                 F(2) F(1) F(1)  F(0)
#                 /  \ 
#               F(1) F(0)
#
