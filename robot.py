import pybullet as p
import pyrosim.pyrosim as pyrosim
from motor import MOTOR
from sensor import SENSOR
class ROBOT:

    def __init__(self):
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

    def sense(self, current_time_step):
        self.current_time_step = current_time_step
        for value in self.sensors:
            sensorObj = self.sensors[value]
            sensorObj.get_value(current_time_step)
        

    def prepare_to_act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def act(self):
        for value in self.motors:
            print(value)
            motorObj = self.motors[value]
            motorObj.set_value(self, self.current_time_step)
