from robot import ROBOT
from world import WORLD
import pybullet as p
import pybullet_data
import constants as c
import time


class SIMULATION:

    def __init__(self, directOrGUI):
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = WORLD()
        self.robot = ROBOT()

    def run(self):
        for current_time_step in range(c.timeSteps):
            p.stepSimulation()
            self.robot.sense(current_time_step)
            self.robot.think()
            self.robot.act()
            time.sleep(c.timeTics)

    def get_fitness(self):
        self.robot.get_fitness()

    def __del__(self):
        p.disconnect()

