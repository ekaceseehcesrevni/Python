import random

value1 = 0
value2 = 0
cardamount = 0
suittype = ""
number1 = random.randint(1,13)
number2 = random.randint(1,13)

if number1 <= 10:
    value1 = number1
else:
    value1 = 10

if number2 <= 10:
    value2 = number2
else:
    value2 = 10

while cardamount < 2:

    suit = random.randint(1, 4)

    if suit == 1:
        suittype = "diamonds"
        cardamount += 1
    elif suit == 2:
        suittype = "clubs"
        cardamount += 1
    elif suit == 3:
        suittype = "hearts"
        cardamount += 1
    else:
        suittype = "spades"
        cardamount += 1
    
    if number1 == 11:
        number1 = "jack"
    elif number1 == 12:
        number1 = "queen"
    elif number1 == 13:
        number1 = "king"
    elif number1 == 1:
        number1 = "ace"

    if number2 == 11:
        number2 = "jack"
    elif number2 == 12:
        number2 = "queen"
    elif number2 == 13:
        number2 = "king"
    elif number2 == 1:
        number2 = "ace"

print(f"You have a {number1} of {suittype}")
print(f"You have a {number2} of {suittype}")

if value1 == 1:
    ace1 = input("You got an ace, do you want it to be worth 1, or 11?")
    if ace1 == "1":
        value1 = 1
    elif ace1 == "11":
        value1 = 11
    else:
        while ace1 != "1" or ace1 != "11":
            ace1 = input("That's not an option, please pick either 1 or 11.")
            if ace1 == "1":
                value1 = 1
                break
            elif ace1 == "11":
                value1 = 11
                break
if value2 == 1:
    ace2 = input("You got an ace, do you want it to be worth 1, or 11?")
    if ace2 == "1":
        value2 = 1
    elif ace2 == "11":
        value2 = 11
    else:
        while ace2 != "1" or ace2 != "11":
            ace2 = input("That's not an option, please pick either 1 or 11.")
            if ace2 == "1":
                value2 = 1
                break
            elif ace2 == "11":
                value2 = 11
                break

startingvalue = value1 + value2

print(f"You have a total of {startingvalue}")

while startingvalue < 21:

    option = input("Do you want to hit or stay?")

    if option == "hit":
        newnumber = random.randint(1,13)
        newsuit = random.randint(1, 4)

        if newsuit == 1:
            newsuittype = "diamonds"
        elif newsuit == 2:
            newsuittype = "clubs"
        elif newsuit == 3:
            newsuittype = "hearts"
        else:
            newsuittype = "spades"

        if newnumber <= 10:
            newvalue = newnumber
        else:
            newvalue = 10

        if newnumber == 11:
            newnumber = "jack"
        elif newnumber == 12:
            newnumber = "queen"
        elif newnumber == 13:
            newnumber = "king"
        elif newnumber == 1:
            newnumber = "ace"

        print(f"You got a {newnumber} of {newsuittype}")

        if newvalue == 1:
            newace = input("You got an ace, do you want it to be worth 1, or 11?")
            if newace == "1":
                newvalue = 1
            elif newace == "11":
                newvalue = 11
            else:
                while newace != "1" or newace != "11":
                    newace = input("That's not an option, please pick either 1 or 11.")
                    if newace == "1":
                        newvalue = 1
                        break
                    elif newace == "11":
                        newvalue = 11
                        break

        startingvalue += newvalue

        print(f"You now have {startingvalue}")

    elif option == "stay":
        break

if startingvalue > 21:
    print("That's a bust!")

elif startingvalue <= 21:
    print("Alright, let's see what the dealer gets!")

    totaldealervalue = 0
    dealervalue = 0

    while totaldealervalue < 17:

        dealernumber = random.randint(1,13)
        dealersuit = random.randint(1, 4)

        if dealersuit == 1:
            dealersuittype = "diamonds"
        elif dealersuit == 2:
            dealersuittype = "clubs"
        elif dealersuit == 3:
            dealersuittype = "hearts"
        else:
            dealersuittype = "spades"

        if dealernumber <= 10:
            dealervalue = dealernumber
        else:
            dealervalue = 10

        if dealernumber == 11:
            dealernumber = "jack"
        elif dealernumber == 12:
            dealernumber = "queen"
        elif dealernumber == 13:
            dealernumber = "king"
        elif dealernumber == 1:
            dealernumber = "ace"

        print(f"The dealer got a {dealernumber} of {dealersuittype}")

        totaldealervalue += dealervalue

    print(f"Which means the dealer got a total of {totaldealervalue}")


if totaldealervalue > 21:
    print("The dealer busted!")
elif totaldealervalue <= 21:
    if totaldealervalue > startingvalue:
        print("You lose")
    elif totaldealervalue > startingvalue:
        print("You win")
    else:
        print("It's a tie")