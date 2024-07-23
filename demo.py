import random
import math

wage_per_hour = 20
full_day = 8
print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======")
print("")

emp_check = math.floor(random.random() * 10) % 2
if emp_check == 0:
    print("Employee is Present")
    print("")
    print(f"The daily wage of Employee is : {wage_per_hour * full_day}")
    print("")
else:
    print("Employee is Absent")
    print("")
    print("The daily wage of Employee is : 0")
    print("")
