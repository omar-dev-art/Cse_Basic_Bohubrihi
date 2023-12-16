employee = {"Name": "Omar", "skills":["python","django","go"],"years of experience":4}
print(employee.get("Name"))

employee["Name"] = "Guest User"
employee["years of experience"]=6

# .update()

employee.update({"Name":"Guest User","years of experience":10})
print(employee)