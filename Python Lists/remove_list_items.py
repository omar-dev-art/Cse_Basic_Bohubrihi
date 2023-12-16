countries = ['Bangladesh', 'india', "usa", "china"]
print(countries)

#using del statement
del countries[1]
print(countries)

del countries[2]
print(countries)

del countries[-1]
print(countries)

#pop method

fruit = ['apple', 'banana', 'mango', 'orange',]
print(fruit)
removed_item = fruit.pop(-1)
print(removed_item)
fruit.pop()
print(fruit)
another_removed_item = fruit.pop(0)
print(fruit)

vowel = ['a','e','i','o','u']
vowel.remove('i')
print(vowel)