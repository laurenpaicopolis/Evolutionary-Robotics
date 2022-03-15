import pyrosim.pyrosim as pyrosim 
length = width = height = 1
x = y = z = 0
import random

def create_world():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[4, 4, 0], size=[length, width, height])
    pyrosim.End()

def generate_body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5, y, 1.5], size=[length, width, height])  # root link
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, y, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, y, -0.5], size=[length, width, height])
    pyrosim.End()

def generate_brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    for sensorValue in range(3):
        for motorValue in (3,4):
            pyrosim.Send_Synapse(sourceNeuronName=sensorValue, targetNeuronName=motorValue, weight=random.uniform(-1,1))

    pyrosim.End()

def create_robot():
    '''pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[x, y, 0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0, 0, 1.0])
    pyrosim.Send_Cube(name="Link1", pos=[0, 0, 0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Link2_Link1", parent="Link1", child="Link2", type="revolute", position=[0, 0, 1.0])
    pyrosim.Send_Cube(name="Link2", pos=[0, 0, 0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Link3_Link2", parent="Link2", child="Link3", type="revolute", position=[0, 0.5, 0.5])
    pyrosim.Send_Cube(name="Link3", pos=[0, 0.5, 0], size=[length, width, height])'''

    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5, y, 1.5], size=[length, width, height]) # root link
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, y, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, y, -0.5], size=[length, width, height])
    pyrosim.End()

generate_body()
generate_brain()
#create_world()
create_robot()
