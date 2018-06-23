#CalcWinner.py
import random

def printIntro():
    print('This program simulates a game between two')
    print('There are two players, A and B')
    print('Probability(a number between 0 and 1)is used')

def getInputs():
    while True:
        probA,probB = eval(input("please input two player win probability:"))
        num = eval(input("how many times game you want to simulate?"))
        if probA<1 and probB<1 and num>0:
            break
        print("输入格式错误请从新输入")
    return probA,probB,num

def simNGames(probA,probB,n):
    if n <= 0:
        return 0,0
    countA = 0
    countB = 0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA, probB)
        if scoreA==15:
            countA += 1
        else:
            countB += 1
    winsA = countA/(countB+countA)
    winsB = countB/(countB+countA)
    return winsA,winsB

def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    throw = "A"
    while not gameOver(scoreA,scoreB):
        if throw == "A":
            if random.random() <= probA:
                scoreA += 1
            throw = "B"
        if throw == "B":
            if random.random() <= probB:
                scoreB += 1
            throw = "A"    
    return scoreA, scoreB

def gameOver(scoreA, scoreB):
    if scoreA>=15 or scoreB>=15:
        return True
    return False

def main():
    printIntro()
    probA,probB,n = getInputs()
    winA, winB = simNGames(probA,probB,n)
    print(winA,winB)

if __name__ == '__main__':
    main()
