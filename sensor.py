import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.timeSteps)
        self.prepare_to_sense()

    def get_value(self, current_time_step):
        self.values[current_time_step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def prepare_to_sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
