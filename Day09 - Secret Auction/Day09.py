import os

print("Welcome to the secret auction program.")
c = "yes"
bids = {}

while c=="yes":
  name = input("What's your name?: ")
  bid = round(float(input("How much are you bidding?: $")), 2)
  bids[name] = bid
  c = input("Is anyone else bidding? ('yes' or 'no'): ")
  os.system('clear||cls')

name = ""
bid = 0
for key in bids:
  if bids[key] > bid:
    bid = bids[key]
    name = key

print(f"{name} won with a bid of ${bid}")