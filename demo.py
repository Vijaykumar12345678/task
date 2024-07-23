import random

class EmployeeWageComputation:
    def __init__(self, company_name, wage, total_no_of_days):
        self.wage_per_hour = wage
        self.full_day = 8
        self.half_day = 4
        self.daily_wage = 0
        self.monthly_wage = 0
        self.counter1 = 0.0
        self.total_hour_present = 0
        self.total_hour_part_time = 0
        self.total_hour_absent = 0
        self.total_hours = 0
        self.company_name = company_name
        self.total_no_of_days = total_no_of_days

    def attendance_check(self):
        self.emp_check = int(random.random() * 10) % 3
        if self.emp_check == 0:
            print(f"{self.company_name}: Employee is Present and is working full time")
            self.total_hour_present += 8
            self.counter1 += 1.0
        elif self.emp_check == 1:
            print(f"{self.company_name}: Employee is Present but working part time")
            self.total_hour_part_time += 4
            self.counter1 += 0.5
        else:
            print(f"{self.company_name}: Employee is Absent")
            self.total_hour_absent += 0
            self.counter1 += 0.0

    def calculate_daily_wage(self):
        if self.emp_check == 0:
            self.daily_wage = self.wage_per_hour * self.full_day
        elif self.emp_check == 1:
            self.daily_wage = self.wage_per_hour * self.half_day
        else:
            self.daily_wage = 0
        print(f"{self.company_name}: The daily wage of Employee is: {self.daily_wage}\n")

    def calculate_monthly_wage(self):
        self.monthly_wage += self.daily_wage
        self.total_hours = self.total_hour_present + self.total_hour_part_time

    def display_monthly_wage(self):
        if self.counter1 >= 20 or self.total_hours >= 100:
            print(f"{self.company_name}: Total working hour while employee is working Full time: {self.total_hour_present}")
            print(f"{self.company_name}: Total working hour while employee is working Part time: {self.total_hour_part_time}")
            print(f"{self.company_name}: Total working hour while employee is Absent: {self.total_hour_absent}")
            print(f"{self.company_name}: The monthly wage is: {self.monthly_wage}")
        else:
            print(f"{self.company_name}: Total working hour while employee is working Full time: {self.total_hour_present}")
            print(f"{self.company_name}: Total working hour while employee is working Part time: {self.total_hour_part_time}")
            print(f"{self.company_name}: The total hours employee worked is: {self.total_hours}")
            print(f"{self.company_name}: The monthly wage is: {self.monthly_wage}")

    def combine_method(self):
        total_no_of_days = int(input("Enter the number of days you were supposed to work (between 1-20) for: "))
        self.total_no_of_days = total_no_of_days

        for i in range(1, self.total_no_of_days + 1):
            print(f"DAY NO: {i}")
            self.attendance_check()
            self.calculate_daily_wage()
            self.calculate_monthly_wage()

        self.display_monthly_wage()

def main():
    print("===== WELCOME TO EMPLOYEE WAGE COMPUTATION ======\n")
    TataMotors = EmployeeWageComputation("Tata Motors", 20, 5)
    Bridgelabz = EmployeeWageComputation("Bridgelabz", 16, 6)
    SamSolutions = EmployeeWageComputation("Sam Solutions", 25, 3)

    user_choice = 'Y'
    while user_choice == 'Y':
        print("Enter your choice 1:Tata Motors 2:Bridgelabz  3:Sam Solutions: ")
        choice = int(input())

        if choice == 1:
            print(f"COMPANY NAME: {TataMotors.company_name}")
            TataMotors.combine_method()
            print("\n")
        elif choice == 2:
            print(f"COMPANY NAME: {Bridgelabz.company_name}")
            Bridgelabz.combine_method()
            print("\n")
        elif choice == 3:
            print(f"COMPANY NAME: {SamSolutions.company_name}")
            SamSolutions.combine_method()
            print("\n")
        else:
            print("Not a valid choice")

        user_choice = input("Do you wish to check any other company details: if yes press 'Y' or else 'N': ").upper()

    print("Thank you for using the service")

if __name__ == "__main__":
    main()
