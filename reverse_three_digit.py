num = int(input("enter a three digit number:"))
a = num % 10
b = num // 10 % 10
c = num // 100
reversed_num = a * 100 + b * 10 + c
print("Reversed number is:", reversed_num)


