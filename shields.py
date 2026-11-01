from dataclasses import dataclass
from random import randint


@dataclass
class ShieldArray:
    max_voids: int
    current_voids: int = None
    collapsed: bool = False


    def __post_init__(self):
        if self.current_voids is None:
            self.current_voids = self.max_voids

    
    def absorb_hit(self):
        """
        Attempt to stop one incoming hit.
        Returns True if shield absorbed it.
        """

        if self.collapsed:
            return False
        
        self.current_voids -= 1

        if self.current_voids <= 0:
            self.current_voids = 0
            self.collapsed = True

        return True
    

    def repair(self, bonus=0):
        recovered = 0
        missing = self.max_voids - self.current_voids

        # attempt to repair collapse first, otherwise shields are non-regeneratable?

        for _ in range(missing):
            roll = randint(1, 6)
            if roll >= 5 - bonus:
                    recovered += 1
                    # don't forget to heat the reactor!


        self.generate_shield(recovered)
        return recovered
    
    def generate_shield(self, count: int=1):
        self.current_voids = min(self.max_voids, self.current_voids+ count)
        return self.current_voids


    def collapse(self):
        self.current_voids = 0
        self.collapsed = True

    def uncollapse(self):
        self.generate_shield()
        self.collapsed = False

  