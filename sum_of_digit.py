num =int(input("Enter a three digit number:"))
a = num % 10
b = num // 10%10
c = num // 100
sum = a+b+c
print("sum of digits is:", sum)