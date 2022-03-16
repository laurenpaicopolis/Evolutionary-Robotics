import solution
import constants as c
import copy


class HILLCLIMBER:

    def __init__(self):
        self.parent = solution.SOLUTION()

    def evolve(self):
        self.parent.evaluate("DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.mutate()
        self.child.evaluate("DIRECT")
        self.Select()
        self.Print()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(str(self.parent.fitness) + ", " + str(self.child.fitness))

    def show_best(self):
        self.parent.evaluate("GUI")
