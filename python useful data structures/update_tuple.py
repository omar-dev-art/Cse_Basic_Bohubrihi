fruits = ("mango", "orange" , "banana")
print(fruits)
fruits = list(fruits)
print(fruits)
fruits.append(1)
fruits.append(2)
fruits.append(3)
fruits[1]="mango"
print(fruits)

fruits = tuple(fruits)
print(fruits)

fruits = list(fruits)
fruits.remove(2)
fruits = tuple(fruits)
print(fruits)