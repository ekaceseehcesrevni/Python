hunger = int(100)
energy = int(100)
health = int(100)
happiness = int(100)
cleanliness = int(100)
print("Hello player! Welcome to this digital pet game!")
pet_type = int(input("First, we need to figure out what type of pet do you want? \t1. Dog \t2. Cat \t3. Rabbit"))
if pet_type == 1:
    pet_type = "dog"
elif pet_type == 2:
    pet_type = "cat"
elif pet_type == 3:
    pet_type = "rabbit"
else:
    while pet_type != 1 or 2 or 3:
        pet_type = int(input("Please choose either 1, 2, or 3"))
        if pet_type < 4 and pet_type >0:
            if pet_type == 1:
                pet_type = "dog"
            elif pet_type == 2:
                pet_type = "cat"
            else:
                pet_type = "rabbit"
            break 
pet_name = input(f"You chose a {pet_type}! Now, what is your pet's name?")
while hunger > 0 or energy > 0 or health > 0 or happiness > 0 or cleanliness > 0:
    print(f"""Here are you pet's stats:
    hunger: {hunger}
    energy: {energy}
    health: {health}
    happiness: {happiness}
    cleanliness: {cleanliness}""")
    choice = int(input("What would you want to do with your pet\t 1. Feed\t 2. Play\t 3. Sleep"))
    if choice == 1:
        print(f"You feed your {pet_type}!")
        hunger += 10
        energy += 5
        happiness += 5
        cleanliness -= 10
    elif choice == 2:
        print(f"You play with your {pet_type}!")
        hunger -= 10
        energy -= 10
        happiness += 15
        health += 5
        cleanliness -= 5
    elif choice == 3:
        print(f"You put your {pet_type} to sleep!")
        hunger -= 10
        energy += 15
        happiness -= 5
        health += 10
    else:
        while choice != 1 or 2 or 3:
            choice = int(input("Please choose either 1, 2, or 3"))
            if choice < 4 and choice >0:
                if choice == 1:
                    print(f"You feed your {pet_type}!")
                    hunger += 10
                    energy += 5
                    happiness += 5
                    cleanliness -= 10
                elif choice == 2:
                    print(f"You play with your {pet_type}!")
                    hunger -= 10
                    energy -= 10
                    happiness += 15
                    health += 5
                    cleanliness -= 5
                else:
                    print(f"You put your {pet_type} to sleep!")
                    hunger -= 10
                    energy += 15
                    happiness -= 5
                    health += 10
                break 
    break