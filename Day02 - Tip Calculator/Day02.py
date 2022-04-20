
print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
num = int(input("How many people are splitting the bill? "))
tip = int(input("What percentage tip would you like to leave? "))

tip /= 100
total += total*tip 
out = round((total/num), 2)

print(f"Each person should pay: ${out}")