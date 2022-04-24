import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
import math
length = width = height = 1
x = 0
y = 0.5
z = 1

class SOLUTION:

    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.zyFitness = 0

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
            print("Fitness Value")
            print(fitnessValue)
        self.zyFitness = float(fitnessValue)
        os.system("rm fitness" + str(self.myID) + ".txt")

    def create_world(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def create_body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0, 1, 2], size=[0.25, 0.5, 1])  # root link

        # SHOULDERS
        pyrosim.Send_Cube(name="ShoulderOne", pos=[0, 0.1, 0], size=[0.2, 0.2, 0.2])
        pyrosim.Send_Cube(name="ShoulderTwo", pos=[0, -0.1, 0], size=[0.2,0.2,0.2])

        # UPPER LEGS
        pyrosim.Send_Cube(name="UpperLegOne", pos=[0, 0, -0.25], size=[0.2, 0.2, 0.5])
        pyrosim.Send_Cube(name="UpperLegTwo", pos=[0, 0, -0.25], size=[0.2, 0.2, 0.5])

        # LOWER LEGS
        pyrosim.Send_Cube(name="LowerLegOne",pos=[0, 0, -0.2], size=[0.2, 0.2, 0.4])
        pyrosim.Send_Cube(name="LowerLegTwo", pos=[0, 0, -0.2], size=[0.2, 0.2, 0.4])

        # ARMS
        pyrosim.Send_Cube(name="ArmOne", pos=[0, 0, -0.375], size=[0.2, 0.2, 0.75])
        pyrosim.Send_Cube(name="ArmTwo", pos=[0, 0, -0.375], size=[0.2, 0.2, 0.75])

        # FEET
        pyrosim.Send_Cube(name="FootOne", pos=[0.05, 0, -0.05], size=[0.3, 0.2, 0.1])
        pyrosim.Send_Cube(name="FootTwo", pos=[0.05, 0, -0.05], size=[0.3, 0.2, 0.1])

        # SHOULDER JOINTS
        pyrosim.Send_Joint(name="Torso_ShoulderOne", parent="Torso", child="ShoulderOne", type="revolute",
                           position=[0, 1.25, 2.2], jointAxis = "0 1 0")
        pyrosim.Send_Joint(name="Torso_ShoulderTwo", parent="Torso", child="ShoulderTwo", type="revolute",
                           position=[0, 0.75, 2.2], jointAxis = "0 1 0")

        # UPPER LEG JOINTS
        pyrosim.Send_Joint(name="Torso_UpperLegOne", parent="Torso", child="UpperLegOne", type="revolute",
                          position=[0, 0.875, 1.5], jointAxis="0 1 0", rotationLimitLower=-math.pi/4, rotationLimitUpper=math.pi/4)
        pyrosim.Send_Joint(name="Torso_UpperLegTwo", parent="Torso", child="UpperLegTwo", type="revolute",
                          position=[0, 1.125, 1.5], jointAxis="0 1 0", rotationLimitLower=-math.pi/4, rotationLimitUpper=math.pi/4)

        # ARM JOINTS
        pyrosim.Send_Joint(name="ShoulderTwo_ArmOne", parent="ShoulderTwo", child="ArmOne", type="revolute",
                          position=[0, -0.2, -0.1], jointAxis="1 0 0")
        pyrosim.Send_Joint(name="ShoulderOne_ArmTwo", parent="ShoulderOne", child="ArmTwo", type="revolute",
                          position=[0, 0.2, -0.1], jointAxis="1 0 0")

        # LOWER LEG JOINTS
        pyrosim.Send_Joint(name="UpperLegOne_LowerLegOne", parent="UpperLegOne", child="LowerLegOne", type="revolute",
                           position=[0,0,-0.5], jointAxis="0 1 0", rotationLimitLower=0, rotationLimitUpper=math.pi/12)
        pyrosim.Send_Joint(name="UpperLegTwo_LowerLegTwo", parent="UpperLegTwo", child="LowerLegTwo", type="revolute",
                           position=[0, 0, -0.5], jointAxis="0 1 0", rotationLimitLower=0, rotationLimitUpper=math.pi/12)

        # FEET JOINTS
        pyrosim.Send_Joint(name="LowerLegOne_FootOne", parent="LowerLegOne", child="FootOne", type="revolute",
                          position=[0, 0, -0.4], jointAxis="0 1 0", rotationLimitLower=-math.pi/12, rotationLimitUpper=math.pi/12)
        pyrosim.Send_Joint(name="LowerLegTwo_FootTwo", parent="LowerLegTwo", child="FootTwo", type="revolute",
                          position=[0, 0, -0.4], jointAxis="0 1 0", rotationLimitLower=-math.pi/12, rotationLimitUpper=math.pi/12)

        pyrosim.End()

    def create_brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="ShoulderOne")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="ShoulderTwo")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="UpperLegOne")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="UpperLegTwo")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="ArmOne")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="ArmTwo")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LowerLegTwo")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="LowerLegOne")
        pyrosim.Send_Sensor_Neuron(name=9, linkName="FootOne")
        pyrosim.Send_Sensor_Neuron(name=10, linkName="FootTwo")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_ShoulderOne")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_ShoulderTwo")
        pyrosim.Send_Motor_Neuron(name=13, jointName="Torso_UpperLegOne")
        pyrosim.Send_Motor_Neuron(name=14, jointName="Torso_UpperLegTwo")
        pyrosim.Send_Motor_Neuron(name=15, jointName="ShoulderTwo_ArmOne")
        pyrosim.Send_Motor_Neuron(name=16, jointName="ShoulderOne_ArmTwo")
        pyrosim.Send_Motor_Neuron(name=17, jointName="UpperLegOne_LowerLegOne")
        pyrosim.Send_Motor_Neuron(name=18, jointName="UpperLegTwo_LowerLegTwo")
        pyrosim.Send_Motor_Neuron(name=19, jointName="LowerLegOne_FootOne")
        pyrosim.Send_Motor_Neuron(name=20, jointName="LowerLegTwo_FootTwo")


        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn+c.numSensorNeurons,
                                     weight= self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, self.weights.shape[0] - 1)
        randomColumn = random.randint(0, self.weights.shape[1] - 1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1

    def setID(self, nextAvailableID):
        self.myID = nextAvailableID
