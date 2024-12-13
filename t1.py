def calculate_gross_salary():
    salary = float(input("Enter the salary amount: "))

    if salary < 0:
        print("Salary cannot be negative.")
        return

    if salary < 10000:
        hra = (salary * 67) / 100
        da = (salary * 73) / 100
    elif salary < 20000:
        hra = (salary * 69) / 100
        da = (salary * 76) / 100
    else:
        hra = (salary * 73) / 100
        da = (salary * 89) / 100

    gross = salary + hra + da
    print(f"Gross Salary: {gross}")

calculate_gross_salary()
