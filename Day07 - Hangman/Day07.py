import os
import res

def clear():
  os.system('clear||cls')

def split(word):
    return [char for char in word]

#initialize the game variables
chosen_word = res.get_word().lower()
chosen_list = split(chosen_word)
length = len(chosen_word)
guessed_list = []
wrong = 0

#fill in the appropriate amount of blanks
for a in chosen_word:
  guessed_list.append("_")

#win and lose result printers
def win():
  print_state()
  print("\n Great Job! You won!!!\n")

def lose():
  print_state()
  print("\nYou were too late... your guy here just done got himself hanged!!!")
  print(f"The word was: {chosen_word}")
  print("Better luck next time!!\n\n You lose!!!!!\n")

#check if both lists match
def check():
  match = True
  for i in range(0, length):
    if not chosen_list[i] == guessed_list[i]:
      match = False
  return match

def print_state():
  clear()
  print(res.logo)
  state = ""
  for a in guessed_list:
    state += (" " + a)
  print("\n"+state+"\n")
  print(res.stages[wrong])
  
while (wrong<6) and not check():
  print_state()
  guess = input("\nGuess a letter:\n").lower()
  contains = False
  for i in range(0, length):
    if chosen_list[i] == guess:
      guessed_list[i] = guess
      contains = True
  if contains == False:
    wrong += 1

if wrong==6:
  lose()
elif check():
  win()
else:
  print("\n\nnot sure what happened here!\n\n")