import pyrosim.pyrosim as pyrosim 

pyrosim.Start_SDF("boxes.sdf")
length = width = height = 1
x = y = z = 0
for y in range(5):
	for x in range(5):
		for num in range(10):
			pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
			z += 1
			width = width * .90
			length = length * .90
			height = height * .90
		x += 1
		width = length = height = 1
		z = 0
	y += 1
	x = 0
pyrosim.End()
