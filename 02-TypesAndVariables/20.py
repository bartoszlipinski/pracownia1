height = float(input('Enter your height in cm: '))
weight = float(input('Enter your weight in kg: '))

# Conversion from cm to m
height = height / 100

bmi = weight/(height**2)

print(f"BMI index: {bmi}")
