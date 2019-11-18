from itertools import permutations

import numpy as np

class Graph:
    def __init__(self, graphMatrix):
        self.__matrix = graphMatrix
        self.__shape = graphMatrix.shape
        self.__alphabet = [1] * (self.__shape[1] - 1) + [0] * (self.__shape[0] - 1)
    
    def getWeight(self, path):
        weight = 0
        i = 0
        j = 0
        for step in path:
            weight += self.__matrix[i, j]
            if step == 0:
                i +=1
            else:
                j += 1
        return weight
    
    def getAllWeights(self):
        permsDict = dict()
        for perm in permutations(self.__alphabet):
            if permsDict.get(perm) is None:
                permsDict[perm] = getWeight(self.__matrix, perm)
        return np.array(permsDict.values())