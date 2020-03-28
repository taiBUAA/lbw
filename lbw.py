import matplotlib.pyplot as plt
import itertools
import random
import copy
class SchellingModel(object):

    def __init__(self,length,t):
        self.matrix = np.zeros((length)*(length)).reshape((length,length))
        self.t = t #threshold value
        self.space = 0 #0 indicates that there is no people
        self.red = 1 #red and blue represent 2 kind of people
        self.blue = 2
        self.length = length
        self.population = 0
        for i in range(length):
            for j in range(length):
                self.matrix[i][j] = random.randint(0,2)
                if self.matrix[i][j] != 0:
                    self.population += 1
    def is_satisfied(self,i,j,kind):
        same_neighbour = -1 # exclude of self
        # create a 3*3 matrix
        neighbour_matrix = self.matrix[i-1 if i-1 >= 0 else 0:i+2,j-1 if j-1 >= 0 else 0:j+2] 
        # count the neighbour for every agent
        for i in range(len(neighbour_matrix)):
            for j in range(len(neighbour_matrix[i])):
                if neighbour_matrix[i][j] == kind:
                    same_neighbour += 1