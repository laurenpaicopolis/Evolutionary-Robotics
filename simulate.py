import pybullet as p
import time
import pybullet_data

#Alters how world is simulated

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")
for value in range(1000000000000):
	p.stepSimulation()
	time.sleep(1/60)
	print(value)
p.disconnect()

