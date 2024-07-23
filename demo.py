import random
import math

def employee_present():
    print("Employee is Present")
    print("")
    print(f"The daily wage of Employee is : {wage_per_hour * full_day * total_no_of_days}")
    print("")

def employee_part_time():
    print("Employee is Present but working part time")
    print("")
    print(f"The daily wage of Employee is : {wage_per_hour * half_day * total_no_of_days}")
    print("")

def employee_absent():
    print("Employee is Absent")
    print("")
    print("The daily wage of Employee is : 0")
    print("")

# Mapping the cases to functions
switch = {
    0: employee_present,
    1: employee_part_time,
    2: employee_absent
}

wage_per_hour = 20
full_day = 8
half_day = 4
total_no_of_days = 20

print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======")
print("")

emp_check = math.floor(random.random() * 10) % 3

# Call the corresponding function based on the value of emp_check
switch.get(emp_check, employee_absent)()
