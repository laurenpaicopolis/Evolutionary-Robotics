import numpy
import matplotlib.pyplot

file1 = "data/BackLegSensorValues.npy"
file2 = "data/FrontLegSensorValues.npy"
backLegSensorValues = numpy.load(file1, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')
frontLegSensorValues = numpy.load(file2, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')
matplotlib.pyplot.plot(backLegSensorValues, label='Back Leg', linewidth=4.5)
matplotlib.pyplot.plot(frontLegSensorValues, label='Front Leg', linewidth=2.0)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
