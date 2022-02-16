import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

file1 = "data/BackLegSensorValues.npy"
file2 = "data/FrontLegSensorValues.npy"
file3 = "data/MotorData.npy"

frequencyF = 11
amplitudeF = numpy.pi/ 6
phaseOffsetF = 0

amplitudeB = numpy.pi/ 6
frequencyB = 11
phaseOffsetB = 0

#Alters how world is simulated
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

targetAnglesF = amplitudeF * numpy.sin(frequencyF * numpy.linspace(0,  2 * numpy.pi, 1000) + phaseOffsetF)
targetAnglesB = amplitudeB * numpy.sin(frequencyB * numpy.linspace(0,  2 * numpy.pi, 1000) + phaseOffsetB)

numpy.save("data/MotorData.npy", targetAnglesB)

for i in range(1000):
	p.stepSimulation()
	pyrosim.Set_Motor_For_Joint(
		# what robot motor should be attached to
		bodyIndex=robotId,
		# what joint motor should be attached to
		jointName='Torso_FrontLeg',
		# how motor will attempt to control motion of joint (position or velocity control)
		controlMode=p.POSITION_CONTROL,
		targetPosition=targetAnglesF[i],
		maxForce=500)
	pyrosim.Set_Motor_For_Joint(
		# what robot motor should be attached to
		bodyIndex=robotId,
		# what joint motor should be attached to
		jointName='Torso_BackLeg',
		# how motor will attempt to control motion of joint (position or velocity control)
		controlMode=p.POSITION_CONTROL,
		targetPosition=targetAnglesB[i],
		maxForce=500)

	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	time.sleep(1/60)
p.disconnect()
numpy.save(file1, backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save(file2, frontLegSensorValues, allow_pickle=True, fix_imports=True)


