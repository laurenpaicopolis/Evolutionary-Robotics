import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

file1 = "data/BackLegSensorValues.npy"
file2 = "data/FrontLegSensorValues.npy"
#Alters how world is simulated
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)
for value in range(100):
	p.stepSimulation()
	backLegSensorValues[value] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[value] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	time.sleep(1/60)
p.disconnect()
numpy.save(file1, backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save(file2, frontLegSensorValues, allow_pickle=True, fix_imports=True)


