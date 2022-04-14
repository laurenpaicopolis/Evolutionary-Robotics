import numpy

# Variables for Bot
frequency = 11
amplitude = numpy.pi/ 6
phaseOffset = 0
backLegFile = "data/BackLegSensorValues.npy"
frontLegFile = "data/FrontLegSensorValues.npy"
motorFile = "data/MotorData.npy"
timeSteps = 1000
maxForceValue = 45
timeTics = 1/500
numberOfGenerations = 5
populationSize = 10
numSensorNeurons = 11
numMotorNeurons = 10
motorJointRange = 0.8
