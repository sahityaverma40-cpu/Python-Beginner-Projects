import random
print("Hi Welcome to the Guessing Number Game.\n You have to guess the number .Let 'start ")
low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))
print(f"\nYou have to guess the number between {low} and {high}. Let 's start")
num = random.randint (low , high)
ch = 7
gc = 0
while ch > 0:
    guess = int(input("Enter your guess:"))
    if guess == num:
        print(f'Correct! THe number is {num} and you guessed it in {gc} attempts.')
        break
    elif gc >= ch and guess != num:
        print(f'Sorry, The number was  {num}. Better luck next time.')
    elif guess > num:
        print("Too high! Try a lower Number.")
    elif guess < num:
        print("Too low ! Try a higher Number.")