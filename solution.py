import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
from icecream import ic

length = width = height = 1
x = 0
y = 0.5
z = 1

class SOLUTION:

    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        # self.weights = self.weights * c.numMotorNeurons - 1

    def start_simulate(self, type):
        self.create_world()
        self.create_body()
        self.create_brain()
        os.system("python3 simulate.py " + type + " " + str(self.myID) + " &")

    def wait_for_simulation_to_end(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        with open("fitness" + str(self.myID) + ".txt", "r") as f:
            fitnessValue = f.read()
        self.fitness = float(fitnessValue)
        os.system("rm fitness" + str(self.myID) + ".txt")

    def create_world(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def create_body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])  # root link

        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Cube(name="BackTwo", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Cube(name="FrontTwo", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Cube(name="LeftLegTwo", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Cube(name="RightLegTwo", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Cube(name="FrontLowerLegTwo", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Cube(name="BackLowerLegTwo", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Cube(name="LeftLowerLegTwo", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Cube(name="RightLowerLegTwo", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[-0.25, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_BackTwo", parent="Torso", child="BackTwo", type="revolute",
                           position=[0.25, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0.25, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_FrontTwo", parent="Torso", child="FrontTwo", type="revolute",
                           position=[-0.25, 0.5, 1], jointAxis="1 0 0")

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-0.5, 0.25, 1], jointAxis="0 1 0")
        pyrosim.Send_Joint(name="Torso_LeftLegTwo", parent="Torso", child="LeftLegTwo", type="revolute",
                           position=[-0.5, -0.25, 1], jointAxis="0 1 0")
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[0.5, 0.25, 1], jointAxis="0 1 0")
        pyrosim.Send_Joint(name="Torso_RightLegTwo", parent="Torso", child="RightLegTwo", type="revolute",
                           position=[0.5, -0.25, 1], jointAxis="0 1 0")

        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute",
                           position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute",
                           position=[1, 0, 0], jointAxis="0 1 0")

        pyrosim.Send_Joint(name="FrontTwo_FrontLowerLegTwo", parent="FrontTwo", child="FrontLowerLegTwo", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Joint(name="BackTwo_BackLowerLegTwo", parent="BackTwo", child="BackLowerLegTwo", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Joint(name="LeftLegTwo_LeftLowerLegTwo", parent="LeftLegTwo", child="LeftLowerLegTwo", type="revolute",
                           position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Joint(name="RightLegTwo_RightLowerLegTwo", parent="RightLegTwo", child="RightLowerLegTwo", type="revolute",
                           position=[1, 0, 0], jointAxis="0 1 0")

        pyrosim.End()

    def create_brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="RightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=9, linkName="BackTwo")
        pyrosim.Send_Sensor_Neuron(name=10, linkName="FrontTwo")
        pyrosim.Send_Sensor_Neuron(name=11, linkName="RightLegTwo")
        pyrosim.Send_Sensor_Neuron(name=12, linkName="LeftLegTwo")
        pyrosim.Send_Sensor_Neuron(name=13, linkName="FrontLowerLegTwo")
        pyrosim.Send_Sensor_Neuron(name=14, linkName="BackLowerLegTwo")
        pyrosim.Send_Sensor_Neuron(name=15, linkName="RightLowerLegTwo")
        pyrosim.Send_Sensor_Neuron(name=16, linkName="LeftLowerLegTwo")

        pyrosim.Send_Motor_Neuron(name=17, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=18, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=19, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=20, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=21, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=22, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=23, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=24, jointName="RightLeg_RightLowerLeg")
        pyrosim.Send_Motor_Neuron(name=25, jointName="Torso_BackTwo")
        pyrosim.Send_Motor_Neuron(name=26, jointName="Torso_FrontTwo")
        pyrosim.Send_Motor_Neuron(name=27, jointName="Torso_LeftLegTwo")
        pyrosim.Send_Motor_Neuron(name=28, jointName="Torso_RightLegTwo")
        pyrosim.Send_Motor_Neuron(name=29, jointName="FrontTwo_FrontLowerLegTwo")
        pyrosim.Send_Motor_Neuron(name=30, jointName="BackTwo_BackLowerLegTwo")
        pyrosim.Send_Motor_Neuron(name=31, jointName="RightLegTwo_RightLowerLegTwo")
        pyrosim.Send_Motor_Neuron(name=32, jointName="LeftLegTwo_LeftLowerLegTwo")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn+c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, self.weights.shape[0])
        randomColumn = random.randint(0, self.weights.shape[1])
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1

    def setID(self, nextAvailableID):
        self.myID = nextAvailableID
