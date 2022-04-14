import pybullet as p
import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from sensor import SENSOR
import os
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import statistics

class ROBOT:

    def __init__(self, solutionID):
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        self.myID = solutionID
        self.upperLegTwoMotors = []
        self.upperLegOneMotors = []
        self.shoulderTwoArm = []
        self.shoulderOneArm = []
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
                self.motors[jointName].set_value(self, desiredAngle)
                if jointName == "Torso_UpperLegTwo":
                    self.upperLegTwoMotors.append(desiredAngle)
                if jointName == "Torso_UpperLegOne":
                    self.upperLegOneMotors.append(desiredAngle)
                if jointName == "ShoulderTwo_ArmOne":
                    self.shoulderTwoArm.append(desiredAngle)
                if jointName == "ShoulderOne_ArmTwo":
                    self.shoulderOneArm.append(desiredAngle)


    def think(self):
        self.nn.update()
        self.nn.Print()

    def get_fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        zCoordinateOfLinkZero = basePosition[2]
        yCoordinateOfLinkZero = basePosition[1]
        sdUpperLegTwo = statistics.pstdev(self.upperLegTwoMotors)
        sdUpperLegOne = statistics.pstdev(self.upperLegOneMotors)

        '''v = self.upperLegOneMotors
        sameOrDifferentLegOne = []
        for n1, n2 in zip(v[:-1], v[1:]):
            if n2 < n1:
                direction = -1
            else:
                direction = 1
            sameOrDifferentLegOne.append(direction)

        reward = 0
        count = 0
        for d1, d2 in zip(sameOrDifferentLegOne[:-1], sameOrDifferentLegOne[1:]):
            if d1 == d2 and count < 10:
                count += 1
                reward += 1
            elif count == 10 and d1 == d2:
                reward -= 1
            elif count == 10 and d1 != d2:
                reward += 1
                count = 0

        v2 = self.upperLegOneMotors
        totalDifLegOne = []
        for n1, n2 in zip(v2[:-1], v2[1:]):
            diff = abs(n1 - n2)
            totalDifLegOne.append(diff)
            count += 1
            if totalDifLegOne[count - 1] == 0:
                reward -= 1
            else:
                reward += 1
            #totalDifLegOne /= (c.timeSteps - 1)

        v2 = self.shoulderOneArm
        totalDifShoulderOne = 0
        for n1, n2 in zip(v2[:-1], v2[1:]):
            diff = abs(n1 - n2)
            totalDifShoulderOne += diff
            # totalDifLegOne /= (c.timeSteps - 1)

        v2 = self.shoulderTwoArm
        totalDifShoulderTwo = 0
        for n1, n2 in zip(v2[:-1], v2[1:]):
            diff = abs(n1 - n2)
            totalDifShoulderTwo += diff
            # totalDifLegOne /= (c.timeSteps - 1)


        v = self.upperLegTwoMotors
        sameOrDifferentLegTwo = []
        direction = 0
        count = 0
        for n1, n2 in zip(v[:-1], v[1:]):
            if n2 < n1 and count > 10:
                while count > 0:
                    direction += 1
                    count -= 1
            elif n2 > n1  and count < 10:
                direction += 1
                count += 1
            elif n2 < n1 and count < 10:
                direction -= 1
            elif n2 > n1 and count > 10:
                direction -= 1
            #sameOrDifferentLegOne.append(direction)

        v = self.upperLegOneMotors
        sameOrDifferentLegTwo = []
        directionTwo = 0
        count = 0
        for n1, n2 in zip(v[:-1], v[1:]):
            if n2 < n1 and count > 10:
                while count > 0:
                    directionTwo += 1
                    count -= 1
            elif n2 > n1 and count < 10:
                directionTwo += 1
                count += 1
            elif n2 < n1 and count < 10:
                directionTwo -= 1
            elif n2 > n1 and count > 10:
                directionTwo -= 1
            # sameOrDifferentLegOne.append(direction)

        rewardTwo = 0
        count = 0
        for d1, d2 in zip(sameOrDifferentLegTwo[:-1], sameOrDifferentLegTwo[1:]):
            if d1 == d2 and count < 10:
                count += 1
                rewardTwo += 1
            elif count == 10 and d1 == d2:
                rewardTwo -= 1
            elif count == 10 and d1 != d2:
                rewardTwo += 1
                count = 0

        
        v3 = self.upperLegTwoMotors
        totalDifLegTwo = 0
        for n1, n2 in zip(v3[:-1], v3[1:]):
            diff = abs(n1 - n2)
            totalDifLegTwo += diff
            #totalDifLegTwo /= (c.timeSteps - 1)

        

        #rewardTwo /= c.timeSteps
        #reward /= c.timeSteps

        v2 = self.upperLegOneMotors
        totalDifLegOne = []
        reward = 0
        count = 0
        for n1, n2 in zip(v2[:-1], v2[1:]):
            diff = abs(n1 - n2)
            totalDifLegOne.append(diff)
            count += 1
            if totalDifLegOne[count - 1] == 0:
                reward -= 1
            else:
                reward += 1
            # totalDifLegOne /= (c.timeSteps - 1)

        v2 = self.upperLegTwoMotors
        totalDifLegTwo = []
        rewardTwo = 0
        count = 0
        for n1, n2 in zip(v2[:-1], v2[1:]):
            diff = abs(n1 - n2)
            totalDifLegTwo.append(diff)
            count += 1
            if totalDifLegTwo[count - 1] == 0:
                rewardTwo -= 1
            else:
                rewardTwo += 1
'''

        #fitnessSum = (totalDifLegOne + totalDifLegTwo) + (yCoordinateOfLinkZero * 1.5)
        #fitnessSum = direction + directionTwo + (zCoordinateOfLinkZero * 50)
        fitnessSum =  yCoordinateOfLinkZero
        with open("tmp" + str(self.myID) + ".txt", "w") as f:
            f.write(str(fitnessSum))
        os.system("mv tmp" + str(self.myID) + ".txt fitness" + str(self.myID) + ".txt")

