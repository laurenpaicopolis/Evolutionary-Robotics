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

    def set_value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            # what robot motor should be attached to
            bodyIndex= robot.robotId,
            # what joint motor should be attached to
            jointName= self.jointName,
            # how motor will attempt to control motion of joint (position or velocity control)
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.maxForceValue)



