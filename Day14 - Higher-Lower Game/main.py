from game_data import data
from art import logo, vs
import random

def getRandom():
  i = random.randint(0, len(data)-1)
  return data[i]

def clear():
  print("\n" * 100)

def format(person):
  return person['name']+", a "+person['description']+", from "+person['country']+"."

def play():
  clear()
  score = 0
  correct = True
  p1 = getRandom()
  p2 = getRandom()
  message = ''
  while correct:
    print(logo)
    print(message)
    print("Compare A: "+format(p1))
    print(vs)
    print("Against B: "+format(p2))
    ans = input("\nWho has more followers? (Type \'A\' or \'B\'): ")
    if (ans=='A' and p1['follower_count']>=p2['follower_count']) or (ans=='B' and p2['follower_count']>=p1['follower_count']):
      score += 1
      p1 = p2 
      p2 = getRandom()
      message = "You were right! Current score = " + str(score) + "\n"
    else:
      correct = False
    clear()
  print(logo)
  print("Sorry, that's wrong... Final Score: " + str(score))

play()