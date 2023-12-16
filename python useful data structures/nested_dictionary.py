courses = {
    1:{
        "Name": "C",
        "duration":3
    },
    2:{
       "Name":"Python",
       "duration":4
    }
}

print(courses)

print(courses[1]["Name"])
print(courses[2]["duration"])

courses[2]["duration"] = 2
courses[2]["Instructor"]= "Two"
print(courses[2])