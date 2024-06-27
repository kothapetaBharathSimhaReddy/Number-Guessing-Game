import math
import random

def main():
    # Taking Inputs
    lower = int(input("Enter Lower bound: "))
    upper = int(input("Enter Upper bound: "))

    # Generating random number between the lower and upper
    x = random.randint(lower, upper)
    total_chances = math.ceil(math.log2(upper - lower + 1))

    print(f"\n\tYou've only {total_chances} chances to guess the integer!\n\n")

    count = 0
    flag = False

    # for calculation of minimum number of guesses depends
    # upon range
    while count < total_chances:
        count += 1

        # Taking guessing number as input
        guess = int(input("Guess a number: "))

        # Condition testing
        if x == guess:
            print(f"Congratulations you did it in {count} try!\n")
            # Once guessed, loop will break
            flag = True
            break
        elif x > guess:
            print("You guessed too small!\n")
        else:
            print("You guessed too high!\n")

    # If Guessing is more than required guesses, shows this
    # output.
    if not flag:
        print(f"\nThe number is {x}\n")
        print("\tBetter Luck Next time!\n")

if __name__ == "__main__":
    main()
