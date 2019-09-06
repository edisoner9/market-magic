
import random

#-----------------------------------------------------------------#

def simulate(sample, start, trials):
    """ sample = number of accounts in the simulation
        start = initial account size
        trials = number of trials we're running for
    """
    
    population = []
    for num in range(sample):
        population.append(start)

    factors = [0, 1.4, 4, .6]        
    day = 0
    
    while day < trials:
        for num in range(sample):
            population[num] *= random.choice(factors)
        day += 1
    
        zeroes = 0
        for num in range(sample):
            if population[num] == 0:
                zeroes += 1
            
        print("Survivors: ", sample - zeroes)
        print("Deaths: ", zeroes)
        print("Average: ", sum(population) / sample)
        print("Max: ", max(population))
        print("Min: ", min(population))
        print("-----------------------------")
    
#-----------------------------------------------------------------#
    
simulate(1000, 10000, 10)


