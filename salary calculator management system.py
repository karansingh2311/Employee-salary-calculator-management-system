# ===== EMPLOYEE SALARY CALCULATOR =====

# List of employees - List ka use
employees = [
    ["Amit", "Manager", 50000],
    ["Riya", "Developer", 40000],
    ["Karan", "Intern", 15000]
]

# Function to calculate salary - Function ka use
def calculate_salary(name, designation, basic_salary):
    hra = 0
    da = 0
    bonus = 0

    # Nested if-else for designation wise allowance
    if designation.lower() == "manager":
        if basic_salary >= 50000:
            hra = basic_salary * 0.30
            da = basic_salary * 0.20
            bonus = 10000
        else:
            hra = basic_salary * 0.25
            da = basic_salary * 0.15
            bonus = 5000

    elif designation.lower() == "developer":
        if basic_salary >= 40000:
            hra = basic_salary * 0.20
            da = basic_salary * 0.15
            bonus = 7000
        else:
            hra = basic_salary * 0.15
            da = basic_salary * 0.10
            bonus = 3000

    elif designation.lower() == "intern":
        hra = basic_salary * 0.10
        da = basic_salary * 0.05
        bonus = 1000

    else:
        print(f"Invalid designation for {name}")
        return 0

    gross_salary = basic_salary + hra + da + bonus
    return gross_salary, hra, da, bonus

# Main Program
print("===== EMPLOYEE SALARY SHEET =====")

# Nested for loop se salary sheet display
for i in range(len(employees)): # outer loop - employee ke liye
    name = employees[i][0]
    designation = employees[i][1]
    basic = employees[i][2]

    # function call
    result = calculate_salary(name, designation, basic)

    if result!= 0:
        gross, hra, da, bonus = result

        print(f"\nEmployee {i+1}:")
        # inner loop - details print karne ke liye (nested loop)
        details = [f"Name: {name}", f"Designation: {designation}", f"Basic: Rs.{basic}"]
        for j in range(len(details)):
            print(details[j])

        print(f"HRA: Rs.{hra}")
        print(f"DA: Rs.{da}")
        print(f"Bonus: Rs.{bonus}")
        print(f"Gross Salary: Rs.{gross}")
        print("--------------------------")

# New Employee Add karna (User Input with Loop)
print("\n===== ADD NEW EMPLOYEE =====")
for k in range(2): # 2 new employees add kar sakte ho
    n = input("\nEnter name (or 0 to stop): ")
    if n == "0":
        break
    d = input("Enter designation (Manager/Developer/Intern): ")
    b = int(input("Enter basic salary: "))

    gross, hra, da, bonus = calculate_salary(n, d, b)
    print(f"-> {n} ka Gross Salary: Rs.{gross}")

print("\nThank You!")