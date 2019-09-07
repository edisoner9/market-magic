
# Simple program illustrating survivorship bias in market performance as
# demonstrated in the book "Fooled by Randomness" by Nassim Nicholas Taleb.

import random, math
import matplotlib as mpl
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------#

def simulate(sample, start, trials):
    """ sample - int representing the number of accounts in the simulation
        start - int representing the initial size of each account
        trials = int representing the number of trials we're running
        
        Returns 6 lists containing data for the number of survivors,
        deaths, maximums, minimums, averages, and medians for each trial
    """
    
    population = []
    for num in range(sample):
        population.append(start)

    factors = [0, 1.4, 2, .7, .5]

    survivors, deaths = [], []
    maximums, minimums = [], []
    averages, medians = [], []        
    
    trial = 0
    while trial < trials:
        for num in range(sample):
            population[num] *= random.choice(factors)
        trial += 1
    
        zero_count = 0
        for num in range(sample):
            if population[num] == 0:
                zero_count += 1
        
        if sample % 2 == 0:
            median = sorted(population)[sample // 2]
        else:
            median = sorted(population)[int(math.ceil((sample / 2)))]

        survivors.append(sample - zero_count)
        deaths.append(zero_count)
        averages.append(sum(population) / sample)
        maximums.append(max(population))
        minimums.append(min(population))
        medians.append(median)

        print("Trial: ", trial)
        print("Survivors: ", sample - zero_count)
        print("Deaths: ", zero_count)
        print("Max: ", max(population))
        print("Min: ", min(population))
        print("Average: ", sum(population) / sample)
        print("Median: ", median)
        print("-----------------------------")
    
    return [survivors, deaths, maximums, minimums, averages, medians]
    
#---------------------------------------------------------------------------#

def graph(data_list):
    """ Takes in a list of data that contains list for the number of survivors,
        deaths, maximums, minimums, averages, and medians (in that order) 
        for a given simulation.
        
        Graphs the data using matplotlib. Returns nothing.
    """
    

    
    
    return
    
#---------------------------------------------------------------------------#

graph(simulate(1000, 10000, 10))













