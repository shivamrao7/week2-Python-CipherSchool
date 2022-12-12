# def sublist_counter(l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count += 1
#     return count
# mixed = [1,2,3,[1,2],[1,23]]
# print(sublist_counter(mixed))


# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as err:
#         print(err)
#     except TypeError as err:
#         print("number must be int or floats")
#     except:
#         print("unexpected error")

# print(divide(10,0))



def fun(a):
    count = 0
    for i in l:
        if type(i)==list:
            count += 1
    return count
l = [1,2,3,[1,3],[],[]]
print(fun(l))