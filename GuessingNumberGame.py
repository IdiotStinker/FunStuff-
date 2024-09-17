from random import randint



def startGame():
    global unanswered
    global answer
    global endGame
    answer = randint(0, 1000)
    unanswered = True
    endGame = False
    while unanswered or endGame:
        guess()

def guess():
    playerGuess = input("Hey! What number do I have? ")
    if playerGuess.isnumeric():
        playerGuess = int(playerGuess)
    else:
        print("WHY DID YOU DO THIS TO ME")
        global endGame
        endGame = True
        return
    if playerGuess == answer:
        print("You are a hero.\n")
        correctAnswer()
    else:
        print("\nYou IDIOT. YOU ACTUALLY SHOULD DIE")
        if playerGuess > answer:
            print("WHAT ARE YOU THINKING? LOWER IT IDIOT\n")
        else:
            print("thou art not high\n")

def correctAnswer():
    global unanswered
    unanswered = False

if __name__ == "__main__":
    while True:
        yes = input("Hey wanna play a game!?!? ")
        yes = yes.lower()
        if yes == "y" or yes == "yes" or yes == "ofc" or yes == "ok" or yes == "of course" or yes == "yeah" or yes == "ya":
            startGame()