import math
from dataclasses import dataclass




@dataclass
class Position:
    x: int
    y: int
    facing: float
    baseSize: int=6

    @property
    def compass_direction(self):
        if self.facing >=337.5 or self.facing < 22.5:
            return "NORTH"
        elif self.facing >= 22.5 and self.facing < 67.5:
            return "NORTHEAST"
        elif self.facing >= 67.5 and self.facing < 112.5:
            return "EAST"
        elif self.facing >= 112.5 and self.facing < 157.5:
            return "SOUTHEAST"
        elif self.facing >= 157.5 and self.facing < 202.5:
            return "SOUTH"
        elif self.facing >= 202.5 and self.facing < 247.5:
            return "SOUTHWEST"
        elif self.facing >= 247.5 and self.facing < 292.5:
            return "WEST"
        else:
            return "NORTHWEST"
        
    
    def rotate(self, degrees):
        self.facing = (self.facing + degrees) % 360


    def distance_to(self, other):
        return math.hypot(
            other.x - self.x,
            other.y - self.y
        )
    