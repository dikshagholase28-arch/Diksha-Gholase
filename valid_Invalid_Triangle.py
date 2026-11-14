a = int(input("enter first side:"))
b = int(input("enter second side:"))
c = int(input("enter third side:"))
if  (a > 0 and b > 0  and c > 0 ) and (a+b>c) and (b+c>a) and (c+a>b):
    print("triangle is valid")
else:
    print("triangle is Invalid")



