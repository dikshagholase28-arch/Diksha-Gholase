num = int(input("Enter a 3 digit number: "))

if num >= 100 and num <= 999:

    a = num % 10
    b = (num // 10) % 10
    c = num // 100

    reverse = a * 100 + b * 10 + c

    if num == reverse:
        print("Palindrome number")
    else:
        print("Not a palindrome number")

else:
    print("Please enter a 3 digit number")