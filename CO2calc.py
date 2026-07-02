print("Welcome to the calculator! Please answer the following questions to calculate your carbon footprint.")
showers=input("How many showers do you take per day?")
stove=input("What kind of stove do you have? (gas/electric/induction)")
meals=input("How many meals a day are cooked?")
lights=input("How many hours per day are the lights on?")
computer=input("How many hours per day are spent on the computer at home?")
transportation=input("What type of transportation do you use? (bus/car/light rail)")
if transportation == "car":
    car=input("What type of car do you have? (gas/electric/hybrid)")
distance=input("How many miles do you travel per day?")
AC=input("How many hours per day is the AC on?")
showers = float(showers) * 1.2
if stove == "gas":
    meals = float(meals) * 0.45
elif stove == "electric":
    meals = float(meals) * 0.3
elif stove == "induction":
    meals = float(meals) * 0.18
lights = float(lights) * 0.0204
computer = float(computer) * 0.06
if transportation == "car":
    if car == "gas":
        distance = float(distance) * 0.4
    elif car == "electric":
        distance = float(distance) * 0.3
    elif car == "hybrid":
        distance = float(distance) * 0.25
elif transportation == "bus":
    distance = float(distance) * 0.726
elif transportation == "light rail":
    distance = float(distance) * 1.361
AC = float(AC) * 1.134
total = float(showers) + float(meals) + float(lights) + float(computer) + float(distance) + float(AC)
print("Your total carbon footprint is: " + str(total) + " kg CO2 per day.")