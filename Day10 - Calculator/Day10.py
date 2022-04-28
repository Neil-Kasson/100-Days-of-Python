import os

def add(n1, n2):
  return n1+n2

def sub(n1, n2):
  return n1-n2

def mult(n1, n2):
  return n1*n2

def div(n1, n2):
  return n1/n2

ops = {
	"+": add,
	"-": sub, 
	"*": mult,
	"/": div
}

first = float(input("What's the first number?: "))
while True:
  op = input("Pick an operation [+ - * /]: ")
  second = float(input("What's the next number?: "))
  res = 0
  if op=="+" or op=="-" or op=="*" or op=="/":
    res = ops[op](first, second)
  else:
    print("Error: Not a valid operator.")
    exit()
  print(f"{first} {op} {second} = {res}")
  c = input(f"Type 'y' to continue calculating with {first}, or type 'n' to start a new calculation: ")
  if c=="y":
    first = res
  elif c=="n":
    os.system('clear||cls')
    first = float(input("What's the first number?: "))
  else:
    os.system('clear||cls')
    exit()