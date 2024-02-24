import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    i = 0
    while guess != random_number:
        i += 1
        guess = int(input(f"Enter the random number between 1 and {x}\n"))

        if guess < random_number:
            print("Guessed Number is too low")
        
        elif guess > random_number:
            print("Guessed number is too high")

    
    print(f"Congrats Guessed the currect number {random_number} in {i} chances")


def computerguess(x):
    low = 1
    high = x
    i = 0
    feedback = ''

    while feedback != 'c':
        i = i + 1
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low

        feedback = input(f"Is the guessed number {guess} too high(h), too low(l),correct(c) ").lower()

        if feedback == 'l':
            low = guess + 1 

        elif feedback == 'h':
            high = guess - 1

    print(f"The computer guessed the correct number {guess} in {i} chances")

        

computerguess(20)
