# Hotdog Eating Contest
# A program to place bets on contestants featured from the 4th of July Nathan's World famous Hotdog eating Contest
# By Tim Murphy 23/7/17

import Epic
import random
import time

# Retrieve user input of winner
def userInput():
    guess = Epic.userString("Pick a winner (Joey, Miki, or Matthew): ")
    return guess.lower()

# User places the bet (bet has to be less than available cash)
def placeBet(cash):
    bet = Epic.userInt("How much would do you want to bet? (cash: $%s) " % cash)
    
    while bet > cash:
        print "You don't have that much money!"
        bet = Epic.userInt("How much would do you want to bet? (cash: $%s) " % cash)
    
    return bet

# Chooses random number    
def getRandomNum():
    num = random.randrange(1, 6)
    return num

# Finds the winner based on who has eaten the highest number of hotdogs    
def findWinner(contestants):
    keys = list(contestants)
    maxKey = keys[0]
    maxValue = contestants[maxKey]
    
    for x in contestants.keys():

        if contestants[x] > maxValue:
            maxKey = x
            maxValue = contestants[x]
    
    return maxKey
    
def main():
    
    cash = 100
    
    while cash > 0:
        Joey = 0
        Miki = 0
        Matthew = 0
        
        guess = userInput()
        bet = placeBet(cash)
        
        print "Ready..."
        time.sleep(1)
        print "Set..."
        time.sleep(1)
        print "Eat!"
# Continues until someone gets to 50
        while Joey < 50 and Miki < 50 and Matthew < 50:
            Joey += getRandomNum()
            Miki += getRandomNum()
            Matthew += getRandomNum()
            
            print "\nJoey has eaten %s Nathan's hotdogs!" % Joey
            print "Miki has eaten %s Nathan's hotdogs!" % Miki
            print "Matthew has eaten %s Nathan's hotdogs!" % Matthew
            print "\nchomp... chomp... chomp!"
            time.sleep(1)
            
        contestants = {"Joey" : Joey, "Miki" : Miki, "Matthew" : Matthew}
        winner = findWinner(contestants)
# Calculates if guess and actual winner are equal
        if guess == winner:
            cash += bet
            print "You guessed right! %s won!" % winner.title()
        else:
            cash -= bet
            print "Sorry, %s didn't win; %s won..." % (guess.title(), winner.title())
        
        print "You have $%s" % cash
    
main()