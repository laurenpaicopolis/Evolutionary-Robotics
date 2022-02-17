import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:

    def __init__(self, jointName):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset
        self.jointName = jointName
        self.prepare_to_act()

    def prepare_to_act(self):
        self.motorValues = self.amplitude * numpy.sin(self.frequency * numpy.linspace(0, 2 * numpy.pi, 1000) + self.offset)
        #self.targetAnglesBack = self.amplitude * numpy.sin(self.frequency * numpy.linspace(0, 2 * numpy.pi, 1000) + self.offset)

    def set_value(self, robot, current_time_step):
        pyrosim.Set_Motor_For_Joint(
            # what robot motor should be attached to
            bodyIndex= robot.robotId,
            # what joint motor should be attached to
            jointName= self.jointName,
            # how motor will attempt to control motion of joint (position or velocity control)
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[current_time_step],
            maxForce=c.maxForceValue
        )

