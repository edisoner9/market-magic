
import random, plot

#--------------------------------------------------------------------#

def martingale(chance, stakes, threshhold, rounds):
    """Takes four positive integers as inputs:
        -percent chance of winning (between 0 and 100)
        -stakes
        -a winnings / loss threshhold
        -maximum number of rounds
    Prints the net profit of the Martingale gambling system with the given
    stakes run until exceeding the threshhold or maximum number of rounds
    along with the highest and lowest points.
    Returns an array of net profit at all points of the run.
    """
    
    count, winnings = 0, 0
    array = []
    initial_stakes = stakes
    while abs(winnings) <= threshhold and count < rounds:
        flip = random.randint(1, 100)
        count += 1
        if flip <= chance:
            winnings += stakes
            array += [winnings]
            stakes = initial_stakes
            print("round = ", count)
            print("winnings = ", winnings)
            print("---" * 3)

        elif flip > chance:
            winnings -= stakes
            array += [winnings]
            stakes *= 2
            print("round = ", count)
            print("winnings = ", winnings)
            print("---" * 3)

    #-----------------------------------------#
    print("Total winnings =", winnings)
    print("Highest point =", max(array))
    print("Lowest point =", min(array))
    
    plot.display(array, "round", "winnings", "Martingale", "graph.png")
    
    return array
 
#--------------------------------------------------------------------#

def avg_winnings(array):
# Average winnings calculator
    return sum(array) / len(array)

#--------------------------------------------------------------------#

# 47% chance of winning each round, starting stakes of 20,
# a threshhold of 5000, and 30 maximum rounds. 
# This could model less-than-perfect blackjack gameplay or roulette.

r1 = martingale(47, 20, 5000, 30)
print("Average winnings = ", avg_winnings(r1))




