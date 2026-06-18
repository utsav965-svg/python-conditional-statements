marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60:
    if age >= 17:
        print("Eligible for Admission")
    else:
        print("Age criteria not satisfied")
else:
    print("Marks criteria not satisfied")
