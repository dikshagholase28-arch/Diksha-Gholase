salary = int(input("Enter basic salary:"))
DA = salary * 10 / 100
TA = salary * 12 / 100
HRA = salary * 15 / 100
total_salary = salary + DA + TA + HRA
print("DA is:", DA)
print("TA is:", TA)
print("HRA is:", HRA)
print("total salary is:", total_salary)
