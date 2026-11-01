from dataclasses import dataclass
from random import randint
from enum import Enum, auto




class ReactorLevel(Enum):
    GREEN = auto()
    YELLOW = auto()
    RED = auto()
    MELTDOWN = auto()




class ReactorEvent(Enum):
    ENGINE_SPLUTTERS = auto()
    SHIELDS_COLLAPSE = auto()
    WEAPONS_OFFLINE = auto()
    SERVO_DAMAGE = auto()
    INTERNAL_EXPLOSION = auto()
    EMERGENCY_VENT = auto()
    REACTOR_MELTDOWN = auto()




@dataclass
class Reactor:
    max_heat: int
    current_heat: int = 0
    residual_heat: int = 0
    pending_heat: int = 0
    vented: bool = False
    shutdown: bool = False


    def boost_movement(self):
        self.add_heat()

    def boost_shields(self):
        self.add_heat()

    def fire_hotweapon(self):
        self.add_heat(2)

    def emergency_turn(self):
        self.add_heat()


    def add_heat(self, amount=1):
        self.current_heat += amount

    def remove_heat(self, amount=1):
        self.current_heat = max(0, self.current_heat - amount)

    def get_heat(self):
        return self.current_heat

    def add_pending_heat(self, amount=1):
        self.pending_heat += amount

    def apply_pending_heat(self, amount=None):
        if amount is None:
            amount = self.pending_heat
        self.add_heat(amount)
        self.pending_heat = 0
        

    def remove_pending_heat(self, amount=1):
        self.pending_heat = max(0, self.pending_heat - amount)

    def get_pending_heat(self):
        return self.pending_heat


    def push_reactor(self):
        self.add_heat(randint(1, 3))

    def cool_reactor(self):
        cool_result = randint(1, 6)
        if cool_result == 1:
            """cooling failure!"""
        elif 2 <= cool_result <= 4:
            self.remove_heat()
        elif cool_result >=5:
            self.remove_heat(2)



    @property
    def level(self) -> str:
        """Current reactor status."""
        ratio = self.current_heat / self.max_heat

        if ratio < 0.4:
            return "GREEN"
        elif ratio < 0.7:
            return "YELLOW"
        elif ratio < 1.0:
            return "RED"
        else:
            return "MELTDOWN"
        
    @property
    def overloaded(self) -> bool:
        """ should we use > or >= here?"""
        return self.current_heat >= self.max_heat

    
    def check_heat(self):
        if self.current_heat > self.max_heat:
            """reactor overload!"""

    def reactor_event(self):
            # reactor overload
            event = randint(1, 6)
            if event == 1:
                """engine splutters"""
            elif event == 2:
                """shields collapse"""
            elif event == 3:
                """weapons offline"""
            elif event == 4:
                """leg servos damaged"""
            elif event == 5:
                """internal explosion"""
                # roll again on this table adding 1 to the resuult each time (can occur recursively!)
            elif event == 6:
                """emergency vent"""
            elif event > 6:
                """reactor meltdown"""