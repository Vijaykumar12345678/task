import random
import math

print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======")

emp_check = math.floor(random.random() * 10) % 2
if emp_check == 0:
    print("Employee is Present")
else:
    print("Employee is Absent")
