numbers = [1, 2, 3, 4, 5, 13, 16, 18, 20]

even_numbers = [i for i in numbers if i%2 == 0]
print(even_numbers)

odd_numbers = [i for i in numbers if i%2 != 0 ]
print(odd_numbers)