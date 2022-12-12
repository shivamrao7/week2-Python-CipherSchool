# scope
x = 5# global variable
def func():
    global x
    x = 7 #  local varibles
    return x

# def funn2():
#     print(x)

# print(x)
# print(func())
# print(x)

print(x)

print(func())
print(x)