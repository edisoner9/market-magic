
import matplotlib.pyplot as pt, numpy as np

def display(array, xlabel, ylabel, title, savefig):
    """Takes in an array of values and plots them sequentially in a line graph"""
    
    x = [num for num in range(len(array))]
    y = array
    pt.plot(x, y)
    
    pt.xlabel(str(xlabel))
    pt.ylabel(str(ylabel))
    pt.title(str(title))
    pt.grid(True)
    pt.savefig(str(savefig))
    pt.show()
    
    
    
