import random

counter = 1
a = int(input("Enter first range: "))
b = int(input("Enter second range: "))
c = int(input("How many dices do you want to roll?: "))

while True:

    for i in range(c):
        roll = random.randint(a,b)
        roll2 = random.randint(a,b)
        print(f"({roll},{roll2})")

    reroll = input("Roll again?(y/n):").lower()
    if reroll == "n":
        print("Thank you for playing!")
        print("Number of dice rolls:", counter)
        break
    elif reroll == "y":
        counter += 1
        continue
        

