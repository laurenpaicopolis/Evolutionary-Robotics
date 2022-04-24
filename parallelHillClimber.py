import solution
import constants as c
import copy
import os
import numpy


class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")
        self.parents = {}
        self.nextAvailableID = 0
        self.data = numpy.random.rand(c.populationSize, c.numberOfGenerations)
        for key in range(c.populationSize):
            value = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.parents[key] = value

    def evolve(self):
        self.evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)

    def Evolve_For_One_Generation(self, currentGen):
        self.Spawn()
        self.mutate()
        self.evaluate(self.children)
        self.Print()
        self.Select(currentGen)

    def Spawn(self):
        self.children = {}
        for key in range(c.populationSize):
            self.children[key] = copy.deepcopy(self.parents[key])
            child = self.children[key]
            child.myID = self.nextAvailableID
            self.nextAvailableID += 1

    def mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self, currentGen):
        for key in range(c.populationSize):
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]
        for col in range(c.populationSize):
           self.data[col][currentGen] = self.parents[col].fitness

    def Print(self):
        print("\n")
        for key in self.parents:
            print(f"Parent: {self.parents[key].fitness}, Child: {self.children[key].fitness} ")

    def evaluate(self, solutions):
        for key in range(c.populationSize):
            solutions[key].start_simulate("DIRECT")
        for key in range(c.populationSize):
            solutions[key].wait_for_simulation_to_end()

    def show_best(self):
        if c.CPGFreq < 400:
            filenameTxt = 'finalSolutionsA.txt'
            filenameNpy = 'finalSolutionsA.npy'
        else:
            filenameTxt = 'finalSolutionsB.txt'
            filenameNpy = 'finalSolutionsB.npy'

        numpy.savetxt(filenameTxt, self.data, delimiter=',')
        with open(filenameNpy,'wb') as f:
            numpy.save(f, self.data)
        first = True
        for key in self.parents:
            if first:
                chosenOne = self.parents[key]
                first = False
            elif chosenOne.fitness > self.parents[key].fitness:
                chosenOne = self.parents[key]
        chosenOne.start_simulate("GUI")
