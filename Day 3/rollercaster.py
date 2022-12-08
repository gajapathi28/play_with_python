print("Hooray!! Welcome to the rollercaster!!")
height = int(input("Enter your height in cms: "))

if height >= 120:
    print("congrats you are eligible to ride the rollercaster")
    age = int(input("Please enter your age: "))
    if age < 12:
        bill = 5
        print("child ticket amount of $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket amount of $7")
    else:
        bill = 12
        print("Adult ticket amount of $12")
    want_photos = input("Would you like to take pictures Y or N ? ")
    if want_photos == "Y":
        bill += 3
        print(f"your total bill should be {bill}")
else:
    print("Sorry!! You need to grow up taller to ride the rollercaster")