import random
import math

lowerB = int(input("Enter lower bound: "))
upperB = int(input("Enter lower bound: "))
target = random.randint(lowerB, upperB)
print("\n\tYou have only ", round(math.log(upperB - lowerB + 1, 2)), "chance(s) to guess the integer\n")

count = 0
while count < round(math.log(upperB - lowerB + 1, 2)):
    count += 1
    guess = int(input("Enter your guess: "))
    if guess > target:
        print("You guessed too high")

    elif guess < target:
        print("you guessed too small")
    elif guess == target:
        print(f"Congratulations, your guess {guess} is right")
        break
    if count >= int(round(math.log(upperB - lowerB + 1, 2)) and guess != target):
        print("\nThe number is %d" % target)
        print("\nBetter Luck next time")