import random

a = int(input("Enter the starting range: "))
b = int(input("Enter the the ending range: "))

ans = random.randint(a,b)
guess_counter = 1
guess_limit = 5

with open("BestScore.txt", "r") as f:
    best_guess = f.read()
    best_guess = int(best_guess)


while True:
    guess = int(input(f"Guess the number (between {a} and {b}): "))
    
    if guess == ans:
        print(f"Congratz! You guessed correctly in {guess_counter} attempts!")
        break
    elif guess > ans:
        guess_counter += 1 
        print("Too high, try again")
    elif guess < ans:
        guess_counter += 1 
        print("Too low, try again")

    if guess_counter == guess_limit + 1:
        print(f"Game Over. The correct guess was {ans}")
        break

if guess_counter < best_guess:
        best_guess = str(guess_counter)

        with open("BestScore.txt", "w") as f:
            f.write(best_guess)

print(f"Best Score: {best_guess} attempts")