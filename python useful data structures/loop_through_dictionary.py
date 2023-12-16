employee ={'Name': 'Omar', 'skills': ['python', 'django', 'go'], 'years of experience': 4, 'company_name': 'Rockstar Games', 'adress': 'Khilgaon', 'Type': 'Permanent'}

#keys() method
print(employee.keys())

#values() method
print(employee.values())

#items()
print(employee.items())

for key in employee.keys():
    print(key,employee[key])
print("----------------------------------")
for key, value in employee.items():
    print(key,value)