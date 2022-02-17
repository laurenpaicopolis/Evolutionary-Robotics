from simulation import SIMULATION
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

simulation = SIMULATION()
simulation.run()

'''
backLegSensorValues = numpy.zeros(c.timeSteps)
frontLegSensorValues = numpy.zeros(c.timeSteps)

targetAnglesFront = c.amplitudeFront * numpy.sin(c.frequencyFront * numpy.linspace(0,  2 * numpy.pi, 1000) + c.phaseOffsetFront)
targetAnglesBack = c.amplitudeBack * numpy.sin(c.frequencyBack * numpy.linspace(0,  2 * numpy.pi, 1000) + c.phaseOffsetBack)

#numpy.save("data/MotorData.npy", targetAnglesBack)

for i in range(c.timeSteps):
	p.stepSimulation()
	pyrosim.Set_Motor_For_Joint(
		# what robot motor should be attached to
		bodyIndex=robotId,
		# what joint motor should be attached to
		jointName='Torso_FrontLeg',
		# how motor will attempt to control motion of joint (position or velocity control)
		controlMode=p.POSITION_CONTROL,
		targetPosition=targetAnglesFront[i],
		maxForce=c.maxForceValue)
	pyrosim.Set_Motor_For_Joint(
		# what robot motor should be attached to
		bodyIndex=robotId,
		# what joint motor should be attached to
		jointName='Torso_BackLeg',
		# how motor will attempt to control motion of joint (position or velocity control)
		controlMode=p.POSITION_CONTROL,
		targetPosition=targetAnglesBack[i],
		maxForce=c.maxForceValue)

	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	time.sleep(c.timeTics)
p.disconnect()
numpy.save(c.backLegFile, backLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save(c.frontLegFile, frontLegSensorValues, allow_pickle=True, fix_imports=True) '''


