import pyrosim.pyrosim as pyrosim
import random
length = width = height = 1
x = y = z = 0

def create_robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5, y, 1.5], size=[length, width, height]) # root link
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, y, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, y, -0.5], size=[length, width, height])
    pyrosim.End()

create_robot()
