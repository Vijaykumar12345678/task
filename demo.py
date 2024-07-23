import random
import math

wage_per_hour = 20
full_day = 8
half_day = 4

print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======")
print("")

emp_check = math.floor(random.random() * 10) % 3
if emp_check == 0:
    print("Employee is Present")
    print("")
    print(f"The daily wage of Employee is : {wage_per_hour * full_day}")
    print("")
elif emp_check == 1:
    print("Employee is Present but working part time")
    print("")
    print(f"The daily wage of Employee is : {wage_per_hour * half_day}")
    print("")
else:
    print("Employee is Absent")
    print("")
    print("The daily wage of Employee is : 0")
    print("")
