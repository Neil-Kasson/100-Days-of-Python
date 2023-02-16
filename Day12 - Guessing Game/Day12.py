import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
diff = input("Choose a difficulty. Type \'easy\' or \'hard\': ")

if diff=='hard':
  tries = 5
elif diff=='easy':
  tries = 10
else:
  tries = 0
  print("that wasn't an option")

num = random.randint(1,100)
lose = True

while tries>0:
  print(f"\nYou have {tries} remaining attempts to guess the number!")
  tries -= 1
  guess = int(input("Make a guess: "))
  if guess>num:
    print("Too high!")
  elif guess<num:
    print("Too low!")
  else:
    print("\nWINNER WINNER CHICKEN DINNER!!!\n")
    tries = 0
    lose = False

if lose:
  print(f"\nThe number was {num}\nYou lose!!!\n")