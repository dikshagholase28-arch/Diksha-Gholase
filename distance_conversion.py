feet = float(input("enter distance in feet:"))
inch = float(input("enter distance in inches:"))
inches = feet * 12 + inch
total_inches = feet * 12 + inch
cm = total_inches * 2.54
print("distance in centimeters:", cm)
print("distance in meters:", cm/100)
