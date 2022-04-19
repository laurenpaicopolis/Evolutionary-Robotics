import numpy

# Variables for Bot
frequency = 11
amplitude = numpy.pi/ 6
phaseOffset = 0
backLegFile = "data/BackLegSensorValues.npy"
frontLegFile = "data/FrontLegSensorValues.npy"
motorFile = "data/MotorData.npy"
timeSteps = 1000
maxForceValue = 50
timeTics = 1/500
numberOfGenerations = 2
populationSize = 5
numSensorNeurons = 17
numMotorNeurons = 16
motorJointRange = 0.2
