import random

class Cell:
    #upon creation cells will have all walls present

    # constructor
    def __init__(self, weights = None):
        self.walls = {'N' : True, 'S' : True, 'W' : True, 'E' : True}
        self.cost = 1

        costList = [1, 3, 5, 8]  # costs for travelling to each node if a weighted maze is to be used
        # for debugging, remove later
        if weights is None:
            weights = [2,3,4,7]

        if weights is not None:
            if len(weights) != len(costList):
                raise ValueError('weights must have same length as costList')
            self.cost = random.choices(costList, weights)[0]


