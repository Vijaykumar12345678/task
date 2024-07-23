import random

class EmployeeWageComputation:
    def __init__(self):
        self.wage_per_hour = 20
        self.full_day = 8
        self.half_day = 4
        self.daily_wage = 0
        self.monthly_wage = 0
        self.counter1 = 0
        self.total_hour_present = 0
        self.total_hour_part_time = 0
        self.total_hour_absent = 0
        self.total_hours = 0

    def attendance_check(self):
        self.emp_check = int(random.random() * 10) % 3
        if self.emp_check == 0:
            print("Employee is Present and is working full time")
            self.total_hour_present += 8
        elif self.emp_check == 1:
            print("Employee is Present but working part time")
            self.total_hour_part_time += 4
        else:
            print("Employee is Absent")
            self.total_hour_absent += 0

    def calculate_daily_wage(self):
        if self.emp_check == 0:
            self.daily_wage = self.wage_per_hour * self.full_day
        elif self.emp_check == 1:
            self.daily_wage = self.wage_per_hour * self.half_day
        else:
            self.daily_wage = 0
        print(f"The daily wage of Employee is: {self.daily_wage}\n")

    def calculate_monthly_wage(self):
        self.monthly_wage += self.daily_wage
        self.total_hours = self.total_hour_present + self.total_hour_part_time

    def display_monthly_wage(self):
        if self.counter1 >= 20 or self.total_hours >= 100:
            print(f"Total working hour while employee is working Full time: {self.total_hour_present}")
            print(f"Total working hour while employee is working Part time: {self.total_hour_part_time}")
            print(f"Total working hour while employee is Absent: {self.total_hour_absent}")
            print(f"The monthly wage is: {self.monthly_wage}")
        else:
            print(f"Total working hour while employee is working Full time: {self.total_hour_present}")
            print(f"Total working hour while employee is working Part time: {self.total_hour_part_time}")
            print(f"The total hours employee worked is: {self.total_hours}")
            print(f"The monthly wage is: {self.monthly_wage}")

def main():
    total_no_of_days = int(input("Enter the number of days you were supposed to work (between 1-20): "))
    e1 = EmployeeWageComputation()

    print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======\n")
    for i in range(1, total_no_of_days + 1):
        print(f"The day is: {i}")
        e1.attendance_check()
        e1.calculate_daily_wage()
        e1.calculate_monthly_wage()

    e1.display_monthly_wage()

if __name__ == "__main__":
    main()
