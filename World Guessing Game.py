import random
name  = input("What is Your Name")
print("Good Luck! ",name)
words = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'sql','R','Data','MYsql','MongoDB','Django']
words = random.choice(words)
print("Guess the Characters ")
guesses =""
turns = 12
while turns > 0:
    failed = 0
    for char in words:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("you Win")
        print("The word is: ", words)
        break
    print()
    guess = input("guess a character:")
    guesses += guess
    if guess not in words:
        turns -= 1
        print("Wrong")
        print("You have",+turns, 'more guesses')
        if turns ==0:
            print("you Loose")


