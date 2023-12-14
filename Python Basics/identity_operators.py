num_one = 2
num_two = 2

print(id(num_one))
print(id(num_two))
print(num_one is num_two)

my_list = []
my_list_two = []

print(id(my_list))
print(id(my_list_two))

print(my_list == my_list_two)
print(my_list is not my_list_two)