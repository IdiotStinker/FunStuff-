#Oh gosh I like her
import random

alphabet = "qwertyuiopasdfghjklzxcvbnm"
alphabet += alphabet.upper()
alphabet += ",.?!\"'/`~()-_+= "

scrambledAlphabet = []
for i in range(len(alphabet)):
    scrambledAlphabet.append("")

for l, letter in enumerate(alphabet):
    while True:
        spot = random.randint(0, len(alphabet)-1)
        if scrambledAlphabet[spot] == "": scrambledAlphabet[spot] = letter; break

alphabet = "".join(scrambledAlphabet)

print(alphabet)