import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dealCard():
  card = random.choice(cards)
  return card

userCards = [dealCard(), dealCard()]
pcCards = [dealCard(), dealCard()]
gameOver = False

'''in: list of cards in hand
   out: score based on hand'''
def getScore(hand):
  score = sum(hand)
  if score==21:
    return 0
  if score>21 and 11 in hand:
    hand[hand.index(11)] = 1
    score = getScore(hand)
  return score

def prompt():
  words = ("\nYour cards: ")
  for i in userCards:
    if i==11:
      words += "[A] "
    else:
      words += ("[" + str(i) + "] ")
  words += "-- Score = " + str(getScore(userCards))
  print(words)
  pcCard = pcCards[0]
  if pcCard == 11:
    pcCard = "A"
  print("Computer's first card: [" + str(pcCard) + "]")

def prompt2():
  words = ("\nYour cards: ")
  for i in userCards:
    if i==11:
      words += "[A] "
    else:
      words += ("[" + str(i) + "] ")
  words += "-- Score = " + str(getScore(userCards))
  print(words)
  words = ("PC cards: ")
  for i in pcCards:
    if i==11:
      words += "[A] "
    else:
      words += ("[" + str(i) + "] ")
  words += "-- Score = " + str(getScore(pcCards))
  print(words)

def end():
  userScore = getScore(userCards)
  if userScore>21:
    print("\nYou went over 21... You lose")
  else:
    while(getScore(pcCards)<17):
      pcCards.append(dealCard())
    pcScore = getScore(pcCards)
    prompt2()
    if pcScore==userScore:
      print("\nIt's a draw!!")
    elif pcScore==0 or (pcScore>userScore and userScore!=0 and pcScore<=21):
      print("\nYou lose!")
    elif userScore==0 or pcScore>21 or userScore>pcScore:
      if userScore==0:
        print("\n***BLACKJACK***")
      else:
        print("\nWinner Winner Chicken Dinner!!!")
    
    

def round():
  gameOver = False
  userScore = getScore(userCards)
  pcScore = getScore(pcCards)

  if (userScore==0 or pcScore==0 or userScore>21):
    gameOver = True
    if userScore>21:
      end()
    else:
      end()
  
  if (gameOver==False):
    prompt()
    goAgain = input("\nWould you like another card? (\'yes\' to continue): ")
    if goAgain=='yes' or goAgain=='y':
      userCards.append(dealCard())
      round()
    else:
      end()

print(art.logo)
round()


############### Our Blackjack House Rules #####################
#   0 = Blackjack
