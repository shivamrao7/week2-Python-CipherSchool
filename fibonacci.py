# 0 1 1 2 3 4 5 8
# for i in range(n):
#     print(i, end = ',')
def fibonacci_seq(n):
    # firstnumber
    a = 0 
    # firstnumber
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b)
    else:
        print(a,b,end=',')
        for i in range(n-2):
            c = a + b   #c=1
            a=b  #a=1
            b = c   #b = 1
            
            c = a+b
            print(b , end = ',')
