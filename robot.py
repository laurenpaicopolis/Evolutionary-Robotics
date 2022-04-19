import pybullet as p
import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from sensor import SENSOR
import os
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:

    def __init__(self, solutionID):
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        self.myID = solutionID
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.prepare_to_act()
        self.prepare_to_sense()
        os.system("rm brain" + str(solutionID) + ".nndf")

    def sense(self, current_time_step):
        for value in self.sensors:
            sensorObj = self.sensors[value]
            sensorObj.get_value(current_time_step)

    def prepare_to_act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def prepare_to_sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                print(desiredAngle)
                self.motors[jointName].set_value(self, desiredAngle)

    def think(self):
        self.nn.update()
        self.nn.Print()

    def get_fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        xCoordinateOfLinkZero = stateOfLinkZero[0][0]
        with open("tmp" + str(self.myID) + ".txt", "w") as f:
            f.write(str(xCoordinateOfLinkZero))
        os.system("mv tmp" + str(self.myID) + ".txt fitness" + str(self.myID) + ".txt")

