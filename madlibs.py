import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f'Guess the number between 1 to {x}: '))
        if guess<random_number:
            print("Sorry, Guess Number Agin. To Low!")
        elif guess>random_number:
            print("Sorry, Guess agin The Number is To high")
        elif guess>x and guess<1:
            print(f"The Number is out the range Number should be in the range 1 to {guess}")
            
        print()
            
    print(f'Congrats You Guessed The Correct Number {guess}')

# x=int(input("Enter the Range of Number You want to paly in Between: "))
# guess(x)


def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback != 'c':
        if low != high:
            guess=random.randint(low,high)
        else:
            guess = low
        feedback=input(f"Is {guess} Too high (h) Too low (l), or Correct (c): ").lower()  
        if feedback == 'h':
            high = guess-1            
        elif feedback == 'l':
            high = guess + 1
    print(f'The computer Guessed Number Correctly {guess}')

x=int(input("Enter A Higest Number: "))
computer_guess(x)

