fruits1 = ['mango ', 'apple']
# fruits1.insert(1,"oranges")
# print(fruits1)
fruits2 = ['graphes', 'apple']
# fruits = fruits1 + fruits2
# print(fruits)

fruits1.extend(fruits2)
fruits1.append(fruits2)
print(fruits1)

a = ['1','2','3','5']
c = ['graphes', 'apple']
a.extend(c)
a.append(c)
print(a)