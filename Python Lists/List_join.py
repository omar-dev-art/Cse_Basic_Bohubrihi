numbers=[1,2,3,4,5]
numbers_two = [6,7,8,9,10]
numbers_three = [100,200,300]

merged_list = numbers + numbers_two + numbers_three
print(merged_list)

# using exted() method

fruits = ['apple','banana','orange']
fruits_two = ['mango']
fruits.extend(fruits_two)
print(fruits)