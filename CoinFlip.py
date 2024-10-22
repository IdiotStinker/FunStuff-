import random
total = 0
tails = 0
rolls = 1000
for i in range(rolls):
    flip1 = random.randint(0, 1) == 1
    flip2 = random.randint(0, 1) == 1
    if (flip1 and flip2):
        continue
    elif ((not flip1 and flip2) or (flip1 and not flip2)):
        total += 1
    elif (not (flip1 and flip2)):
        total += 1
        tails += 1

percent = round((tails / total) * 100, 2)
print (f"Out of {rolls} rolls, there were only {total} amount with atleast one tails.")
print (f"Out of {total} rolls with atleast one tails, the probablity that both were tails was {percent} or {tails} out of {total}.")