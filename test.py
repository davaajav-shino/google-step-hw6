#!/usr/bin/env python3
import sys
import math
from itertools import *

import solver_greedy
from common import print_solution, read_input
from intersect import doIntersect

FILENAME = 'input_6.csv'
INPUT = read_input(FILENAME)
LENGTH = len(INPUT)
solution = solver_greedy.solve(INPUT)

class Tour(object):

    def __init__(self, solution):
        self.tour_list = solution
        self.tour_list.append(solution[0])

        self.dist = [[0] * LENGTH for i in range(LENGTH)]
        for i in range(LENGTH):
            for j in range(LENGTH):
                self.dist[i][j] = self.dist[j][i] = solver_greedy.distance(INPUT[i], INPUT[j])

    def getTour(self):
        return self.tour_list

    def intersectsWithSubsequentEdge(self, i):
        A, B = self.tour_list[i], self.tour_list[i+1]
        for j in range(i+1, LENGTH):
            C, D = self.tour_list[j], self.tour_list[j+1]
            if doIntersect(INPUT[A], INPUT[B], INPUT[C], INPUT[D]):
                return j 

    def redraw(self, i_1, j):
        length = j+1 - i_1
        for k in range(length/2):
            tmp = self.tour_list[i_1 + k]
            self.tour_list[i_1 + k] = self.tour_list[j-k]
            self.tour_list[j-k] = tmp

    def getDistance(self):
        tourDistance = 0
        for cityIndex in range(LENGTH):
            fromCity = self.tour_list[cityIndex]
            destinationCity = self.tour_list[cityIndex + 1]
            tourDistance += self.dist[fromCity][destinationCity]
        return tourDistance

def solve():
    tour = Tour(solution)
    i = 0
    while (i < LENGTH):
        j = tour.intersectsWithSubsequentEdge(i)
        if j:
            tour.redraw(i+1, j)
        i+=1
    print tour.getTour()
    print tour.getDistance()


if __name__ == '__main__':
    solve()
    



