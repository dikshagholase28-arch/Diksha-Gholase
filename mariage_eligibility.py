gender = input("Enter gender: ")
age = int(input("Enter age: "))

if gender == "male" and age >= 21:
    print("Eligible for marriage")

elif gender == "female" and age >= 18:
    print("Eligible for marriage")

else:
    print("Not eligible for marriage")