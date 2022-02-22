import pybullet as p
import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:

    def __init__(self):
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)

    def sense(self, current_time_step):
        for value in self.sensors:
            sensorObj = self.sensors[value]
            sensorObj.get_value(current_time_step)
        

    def prepare_to_act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].set_value(self, desiredAngle)

    def think(self):
        self.nn.update()
        self.nn.Print()

