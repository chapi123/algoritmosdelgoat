def fibonacci (n) :
    listt = [0,1]
    for i in range(n):
        result = listt[i+1] + listt[i]
        listt.append(result) 
    return listt[n]

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
