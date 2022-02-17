import numpy

frequency = 11
amplitude = numpy.pi/ 6
phaseOffset = 0

'''amplitudeBack = numpy.pi/ 6
frequencyBack = 11
phaseOffsetBack = 0'''

backLegFile = "data/BackLegSensorValues.npy"
frontLegFile = "data/FrontLegSensorValues.npy"
motorFile = "data/MotorData.npy"

timeSteps = 1000

maxForceValue = 500
timeTics = 1/60
