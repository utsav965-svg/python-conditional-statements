salary = int(input("Enter salary: "))
experience = int(input("Enter years of experience: "))

if salary >= 30000:
    if experience >= 2:
        print("Eligible for Bonus")
    else:
        print("Experience not enough")
else:
    print("Salary criteria not met")
