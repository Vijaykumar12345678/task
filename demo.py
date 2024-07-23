import random
import math

def main():
    wage_per_hour = 20
    full_day = 8
    half_day = 4
    daily_wage = 0
    monthly_wage = 0

    print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======")
    print("")
    total_no_of_days = int(input("Enter the number of days you were supposed to work (between 1-20): "))
    total_hours = total_no_of_days * full_day
    counter = 0

    for i in range(1, total_no_of_days + 1):
        emp_check = math.floor(random.random() * 10) % 3
        if emp_check == 0:
            print(f"Employee is Present on day and is working full time: {i}")
            daily_wage = wage_per_hour * full_day
            print(f"The daily wage of Employee is: {daily_wage}")
            print(" \n ")
            counter += 1
        elif emp_check == 1:
            print(f"Employee is Present but working part time on day: {i}")
            daily_wage = wage_per_hour * half_day
            print(f"The daily wage of Employee is: {daily_wage}")
            print(" \n ")
        else:
            print(f"Employee is Absent on day: {i}")
            daily_wage = 0
            print(f"The daily wage of Employee is: {daily_wage}")
            print(" \n ")

        monthly_wage += daily_wage

    print("\n")
    if total_hours >= 100 or counter >= 20:
        print(f"The monthly wage of employee is: {monthly_wage}")
    else:
        print(f"The monthly wage of employee is: {monthly_wage}")

if __name__ == "__main__":
    main()
