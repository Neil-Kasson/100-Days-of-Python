import random
import art

pc = random.randint(0,2)
list = [art.rock, art.paper, art.scissors]

player = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
if not (player=="0" or player=="1" or player=="2"):
  print("\nThat's not a choice, dummy... you lose!!!")
else:
	player = int(player)
	print(list[player])
	print("Computer chose: \n" + list[pc])
	if (player==0 and pc==1) or (player==1 and pc==2) or (player==2 and pc==0):
		print("Haha... You lose!")
	elif player==pc:
		print("Damn... it's a tie!!")
	else:
		print("Nice... You won!!!")
