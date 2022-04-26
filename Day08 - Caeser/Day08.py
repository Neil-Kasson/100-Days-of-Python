import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def crypt(txt, shft):
    out = ""
    for letter in txt:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                out += alphabet[(position + shft) % 26]
            else:
                out += alphabet[(position - shft) % 26]
        else:
            out += letter
    print(f"\nThe encoded output is: \n\"{out}\"\n")

go = "yes"

while (go == "yes" or go == "y"):
    os.system('clear||cls')
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if not (direction == "encode" or direction == "decode"):
        print("-[-]- Error: That's not an option -[-]-")
        exit()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    crypt(text, shift)
    go = input("Would you like to go again? (yer or y to continue)\n").lower()

os.system('clear||cls')
print("\n Have a nice day!!\n")
