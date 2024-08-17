print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm: "))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age: "))
    if age < 12:
        print("Price for the ticket is $5")
    elif age < 18:
        print("Price for the ticket is $10")
    else:
        print("Price for the ticket is $15")
else:
    print("Sorry, you have to grow taller before you can ride")
