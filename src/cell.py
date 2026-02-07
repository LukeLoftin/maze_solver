class Cell:
    #upon creation cells will have all walls present

    # constructor
    def __init__(self, cost):
        self.cost = cost
        self.walls = {'N' : True, 'S' : True, 'W' : True, 'E' : True}