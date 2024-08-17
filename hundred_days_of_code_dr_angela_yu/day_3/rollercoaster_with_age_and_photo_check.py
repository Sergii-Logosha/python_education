print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm: "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age: "))
    if age < 12:
        bill = 5
        print("Child ticket is $5")
    elif age < 18:
        bill = 10
        print("Youth ticket is $10")
    else:
        bill = 15
        print("Adult ticket is $15")

    is_photo_requested = input("Do you want to get a photo(y/n): ")
    if is_photo_requested == "y":
        bill += 3

    print(f"The total bill is: ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")