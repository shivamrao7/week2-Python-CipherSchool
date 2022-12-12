numbers = list(range(1,11))
# print(numbers)
# poped_item = numbers.pop()
# print(numbers)
# print(numbers.index(1))
# print(numbers.index(1,3,14))

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))