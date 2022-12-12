#  Function inside function
# greater(a,b) ---> a or b
# greater(a or b, c) 

# def greater(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
    
#     return c

def new_greatest(a,b,c):
    # bigger = greater(a,b)
    return max(max(a,b),c)
# kiss - keep it smple stupid
print(new_greatest(1000,200,30))