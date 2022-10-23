fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
print('\nDaftar/List Buah....')
print(fruits)

for x in fruits:
  if "a" in x:
    newlist.append(x)

print('\nDengan for x ... daftar buah yang ada huruf "a" ')
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print('\nDengan cara List Comprehension ....')
print(newlist)