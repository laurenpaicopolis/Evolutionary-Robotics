import pybullet as p
import time

physicsClient = p.connect(p.GUI)
for value in range(0,1000):
	p.stepSimulation()
	time.sleep(1/60)
	print(value)
p.disconnect()

