#total marks greater than equal to 80 than grade A+
# total marks greater than equal to 40 and less than 80 then grade B
# otherwise grade F

total_marks = 85

if total_marks >= 80:
    print("A+")
elif total_marks >= 40 and total_marks<80 :
    print("B")
elif total_marks >= 40 and total_marks<60 :
    print("C")
else :
    print("F")