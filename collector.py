import logging
import sys
from optparse import OptionParser
from logutils import initLogging,getLogger
from ant import Ant
from ants import FOOD

class CollectorAnt(Ant):
    def __init__(self, position):
        Ant.__init__(self, position)
        self.path = []
        self.index = 0
        self.target = None

    def suggestMove(self, ants, colony):
        if(len(self.path) == 0):
            targets = [colony.collectors[i].target for i in range(0, len(colony.collectors))]
            (self.path, self.target) = ants.get_nearest_food(self.position, targets)
            self.index = 0

        if(len(self.path) != 0 and self.path[self.index][0] != self.getPosition()):
            getLogger().debug("Reset" + str(self.getPosition()) + ", " + str(self.path[self.index][0]))
            targets = [colony.collectors[i].target for i in range(0, len(colony.collectors))]
            (self.path, self.target) = ants.get_nearest_food(self.position, targets)
            self.index = 0

        if(len(self.path) != 0):
            direction = self.path[self.index][1]
            self.index = self.index + 1
            if(self.index == len(self.path)):
                self.path = []
                self.target = None
            return direction
        else:
            return '#'


