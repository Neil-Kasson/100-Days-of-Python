import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
let = int(input("How many letters would you like in your password?\n")) 
sym = int(input(f"How many symbols would you like?\n"))
num = int(input(f"How many numbers would you like?\n"))

p = ""

for n in range(0, let):
  p += letters[random.randint(0, len(letters)-1)]
for n in range(0, sym):
  p += symbols[random.randint(0, len(symbols)-1)]
for n in range(0, num):
  p += numbers[random.randint(0, len(numbers)-1)]

l = list(p)
random.shuffle(l)
p = ''.join(l)

print("Here's your password: "+p)