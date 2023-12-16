employee ={'Name': 'Omar', 'skills': ['python', 'django', 'go'], 'years of experience': 4, 'company_name': 'Rockstar Games', 'adress': 'Khilgaon', 'Type': 'Permanent'}

#del keyword

del employee['adress']
print(employee)

# pop() method
print(employee.pop('skills'))
print(employee)