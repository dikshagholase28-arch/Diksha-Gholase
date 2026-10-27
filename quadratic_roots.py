import math
a = int( input("Enter a:"))
b = int( input("Enter b:"))
c = int( input("Enter c:"))

d = b*b - 4*a*c

root1 = (-b + math.sqrt(d)) / (2*a)
root2 = (-b - math.sqrt(d)) / (2*a)

print("First root=",root1)
print("Second root=",root2)
