numbers = [10,20,30,40,50,60]

#using copy() method

numbers_backup1 = numbers.copy()
print(numbers_backup1)

#using list(literable) function

copy_numbers = list(numbers)
print(copy_numbers)

#using slice

slice_numbers = numbers[:]
print(slice_numbers)