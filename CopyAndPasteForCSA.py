def wave(name):
    return "hi"+name

# Is the value "hi Nathaniel"
wave("Nathaniel")

groceryList = """Pie
Cheese
Chocolate
Anchovies"""

groceryList.split("\n")
["Pie", "Cheese", "Chocolate", "Anchovies"]

declarationOfIndependance = "We the People, in order to form a more perfect Union".split()
#print(declarationOfIndependance[-2])
"perfect"

footballScores = """Houston-Texans vs Pittsburgh-Steelers, 7 to 6
New England-Patriots vs Los Angeles-Chargers, 16 to 3
San Francisco-49ers vs Philadelphia-Eagles, 23 to 10"""
#team = ???
#print("The " + team + " are the best!")


footballScores.split(" ")[0].split(" - ")[0][1]
#footballScores.split("\n")[3].split(" vs ")[1].split("-")[0]
footballScores.split("\n")[2].split(" vs ")[0].split("-")[1]
#footballScores.split("\n")[2].split()[0].split()[1]

float("410.23")
410.23
int("13  ")
13
#print(int("7") * float("2.4"))
16.8

#def doSchool()
#for i in range(5):
#    doSchool()

names = ["Henry", "Jim", "Destiny Testiny"]
#for name in names: print(name)

numbers = [51, 30, 1, 62.5]
favoriteNumSpot = None
for index, number in enumerate(numbers):
    if number == 62.5:
        favoriteNumSpot = index


#day2
yes =numbers.pop()

def removeThird(items):
    return items.pop(2)

words=["Hello", "Goo'bye", "Strange"]


#list.insert()

cars = ["honda", "toyota", "KIA", "lamborghini", "BMW" ]
cars.sort() # Capital first, then A-Z: BMW, KIA, Honda...
#print(cars)
cars.sort(key=str.lower) # W/o capitals: BMW, honda...
#print(cars)
cars.sort(key=len, reverse=True) # Long to short: lamborghini, toyota...
#print(cars)
cars.sort(key=len) # KIA is originally first so it is ahead of BMW
#print(cars)

def order(layer):
    return list(layer).count("#")

pyramid = """#######
   #    
 #####  
  ###   """

pyramid = pyramid.split("\n")
pyramid.sort(key=order)
#print(pyramid)

#for level in pyramid: print(level)
import math
#math.pow()
#print(0x100)

user_input = input("pick a number")

is_prime = True
for i in range(2, int(user_input)):
    if int(user_input) % i == 0 :
        is_prime = False
        break #break out of the for loop since the number isn't prime

if is_prime:
   print("Your number is prime")
else:
   print("your number is not prime")