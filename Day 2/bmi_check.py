# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight / height ** 2)
your_bmi = int(BMI)
if your_bmi < 18.5:
    print(f"Your BMI is {your_bmi}, you are slightly underwight")
elif your_bmi < 25:
    print(f"Your BMI is {your_bmi}, you have a normal weight" )
elif your_bmi < 30:
    print(f"Your BMI is {your_bmi}, you are slightly overweight" )
elif your_bmi < 35:
    print(f"Your BMI is {your_bmi}, you are obese" )
else:
    print(f"Your BMI is {your_bmi}, you are clinically obese" )