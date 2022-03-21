import solution
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")
        self.parents = {}
        self.nextAvailableID = 0
        for key in range(c.populationSize):
            value = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            self.parents[key] = value

    def evolve(self):
        self.evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.mutate()
        self.evaluate(self.children)
        self.Print()
        self.Select()

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

    def Select(self):
        for key in range(c.populationSize):
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]

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
        first = True
        for key in self.parents:
            if first:
                chosenOne = self.parents[key]
                first = False
            elif chosenOne.fitness > self.parents[key].fitness:
                chosenOne = self.parents[key]
        chosenOne.start_simulate("GUI")
