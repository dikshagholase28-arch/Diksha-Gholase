import random

userid = input("Enter user id: ")
password = input("Enter password: ")

if userid == "admin" and password == "1234":
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)

    num = int(input("Enter captcha: "))

    if num == captcha:
        print("Login successful")
    else:
        print("Login failed")

else:
    print("Invalid userid or password")