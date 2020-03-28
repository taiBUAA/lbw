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
       # judge
        if same_neighbour >= self.t:
            return True
        else:
            return False
    def random_find(self):
        i = random.randint(0,self.length-1)
        j = random.randint(0,self.length-1)
        while self.matrix[i][j] != 0:
            i = random.randint(0, self.length - 1)
            j = random.randint(0, self.length - 1)
        return (i,j)
    def move(self):
        satisfy = 0
        for i in range(self.length):
            for j in range(self.length):
                if self.matrix[i][j] != self.space:
                    people_kind = self.matrix[i][j]
                    judge = self.is_satisfied(i,j,people_kind)
                    if judge == 0:
                        (p,q) = self.random_find()
                        self.matrix[p][q] = people_kind
                        self.matrix[i][j] = self.space
                    else:
                        satisfy += 1
        return satisfy
    def draw(self,time,satisfy = 0):
        redx = []
        bluex = []
        redy = []
        bluey = []
        for i in range(self.length):
            for j in range(self.length):
                if self.matrix[i][j] == self.blue:
                    bluex.append(i)
                    bluey.append(j)
                elif self.matrix[i][j] == self.red:
                    redx.append(i)
                    redy.append(j)
        plt.scatter(redx,redy,c = 'r',marker='.',linewidths=0)
        plt.scatter(bluex,bluey,c = 'b',marker='.',linewidths=0)
        if satisfy==0:
            plt.title('Initial')
        else:
            title = str(time)+' times satisfy:'+str(float(satisfy)/float(self.population))
            plt.title(title)
        plt.show()
if __name__ == '__main__':
    s = SchellingModel(150,4)
    s.draw(0)
    i = 0
    while(1):
        satisfy = s.move()
        i+=1
        s.draw(i,satisfy)