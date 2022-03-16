import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
length = width = height = 1
x = y = z = 0

class SOLUTION:

    def __init__(self):
        self.weights = numpy.random.rand(3, 2)
        self.weights = self.weights * 2 - 1

    def evaluate(self, type):
        self.create_world()
        self.create_body()
        self.create_brain()
        f = open("fitness.txt", "r")
        fitnessValue = f.read()
        self.fitness = float(fitnessValue)
        f.close()
        os.system("python3 simulate.py " + type)

    def create_world(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[4, 4, 0], size=[length, width, height])
        pyrosim.End()

    def create_body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5, y, 1.5], size=[length, width, height])  # root link
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[1, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, y, -0.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[2, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, y, -0.5], size=[length, width, height])
        pyrosim.End()

    def create_brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Motor_Neuron(name=0, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=1, jointName="Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in (0, 1):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3,
                                     weight= self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1
