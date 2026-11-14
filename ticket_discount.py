totalprice = 0

# First Person
age1 = int(input("Enter age of first person: "))
tk1 = float(input("Enter ticket amount of first person: "))

if age1 > 59:
    disc = (tk1 / 100) * 50
    tk1 = tk1 - disc
    totalprice = totalprice + tk1
    print("You will get discount of", disc)

elif age1 < 12:
    disc = (tk1 / 100) * 30
    tk1 = tk1 - disc
    totalprice = totalprice + tk1
    print("You will get discount of", disc)

else:
    totalprice = totalprice + tk1


# Second Person
age2 = int(input("Enter age of second person: "))
tk2 = float(input("Enter ticket amount of second person: "))

if age2 > 59:
    disc = (tk2 / 100) * 50
    tk2 = tk2 - disc
    totalprice = totalprice + tk2
    print("You will get discount of", disc)

elif age2 < 12:
    disc = (tk2 / 100) * 30
    tk2 = tk2 - disc
    totalprice = totalprice + tk2
    print("You will get discount of", disc)

else:
    totalprice = totalprice + tk2


# Third Person
age3 = int(input("Enter age of third person: "))
tk3 = float(input("Enter ticket amount of third person: "))

if age3 > 59:
    disc = (tk3 / 100) * 50
    tk3 = tk3 - disc
    totalprice = totalprice + tk3

elif age3 < 12:
    disc = (tk3 / 100) * 30
    tk3 = tk3 - disc
    totalprice = totalprice + tk3

else:
    totalprice = totalprice + tk3


# Fourth Person
age4 = int(input("Enter age of fourth person: "))
tk4 = float(input("Enter ticket amount of fourth person: "))

if age4 > 59:
    disc = (tk4 / 100) * 50
    tk4 = tk4 - disc
    totalprice = totalprice + tk4

elif age4 < 12:
    disc = (tk4 / 100) * 30
    tk4 = tk4 - disc
    totalprice = totalprice + tk4

else:
    totalprice = totalprice + tk4


# Fifth Person
age5 = int(input("Enter age of fifth person: "))
tk5 = float(input("Enter ticket amount of fifth person: "))

if age5 > 59:
    disc = (tk5 / 100) * 50
    tk5 = tk5 - disc
    totalprice = totalprice + tk5

elif age5 < 12:
    disc = (tk5 / 100) * 30
    tk5 = tk5 - disc
    totalprice = totalprice + tk5

else:
    totalprice = totalprice + tk5

print("Total ticket price =", totalprice)