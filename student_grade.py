m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))
m4 = int(input("Enter subject 4 marks: "))
m5 = int(input("Enter subject 5 marks: "))

total = m1 + m2 + m3 + m4 + m5

percentage = total / 5

print("Total marks:", total)
print("Percentage:", percentage)

if percentage >= 60:
    print("First Class")

elif percentage >= 50:
    print("Second Class")

elif percentage >= 40:
    print("Pass Class")

else:
    print("Fail")