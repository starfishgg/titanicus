from dataclasses import dataclass
from reactor import Reactor
from shields import ShieldArray
from weapon import WeaponTemplate
from enum import Enum
from position import Position
from entity import BattlefieldEntity




class LocationType(Enum):
    HEAD = "head"
    BODY = "body"
    LEGS = "legs"  # For simplicity, we are treating both legs as one location for now. This can be expanded later if needed.




class WeaponMount(Enum):
    LEFT_ARM = "left_arm"
    RIGHT_ARM = "right_arm"
    CARAPACE_LEFT = "carapace_left"
    CARAPACE_RIGHT = "carapace_right"
    CARAPACE_CENTER = "carapace_centre"



@dataclass(frozen=True)
class TitanTemplate:
    head: tuple[int, int]  # armor, hp
    body: tuple[int, int]
    legs: tuple[int, int]
    voids: int
    reactor_max: int
    weapon_slots: int
    weapon_mounts: tuple[WeaponMount, ...]
    speed: int

WARHOUND = TitanTemplate(
    head=(3, 4), # armor, hp
    body=(6, 10),
    legs=(5, 8),
    voids=4,
    reactor_max=8,
    weapon_slots=2,
    weapon_mounts=(
        WeaponMount.LEFT_ARM,
        WeaponMount.RIGHT_ARM
    ),
    speed=30,
)

REAVER = TitanTemplate(
    head=(4, 6), # armor, hp
    body=(8, 15),
    legs=(7, 12),
    voids=6,
    reactor_max=10,
    weapon_slots=3,
    weapon_mounts=(
        WeaponMount.LEFT_ARM,
        WeaponMount.RIGHT_ARM,
        WeaponMount.CARAPACE_CENTER
    ),
    speed=20,
)

WARLORD = TitanTemplate(
    head=(5, 8), # armor, hp
    body=(12, 25),
    legs=(10, 18),
    voids=8,
    reactor_max=12,
    weapon_slots=4,
    weapon_mounts=(
        WeaponMount.LEFT_ARM,
        WeaponMount.RIGHT_ARM,
        WeaponMount.CARAPACE_LEFT,
        WeaponMount.CARAPACE_RIGHT
    ),
    speed=15,
)


TITAN_TEMPLATES = {
    "warhound": WARHOUND,
    "reaver": REAVER,
    "warlord": WARLORD,
}




class Location:
    def __init__(self, location_type: LocationType, armour: int, hp: int):
        self.type = location_type
        self.armour = armour
        self.max_hp = hp
        self.hp = hp

    @property
    def destroyed(self):
        return self.hp == 0
    
    def get_location(self, location_type: LocationType):
        return self.locations[location_type]
    
    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)
    



class Titan(BattlefieldEntity):
    def __init__(self, name, titan_type, owner, position):
        super().__init__(name, owner, position)

        self.class_name = titan_type
        self.order = None

        profile = TITAN_TEMPLATES[titan_type]

        self.locations = {
            LocationType.HEAD: Location(LocationType.HEAD, *profile.head),
            LocationType.BODY: Location(LocationType.BODY, *profile.body),
            LocationType.LEGS: Location(LocationType.LEGS, *profile.legs),
        }

        self.shields = ShieldArray(profile.voids)

        self.reactor = Reactor(profile.reactor_max)

        self.weapon_mounts = {
            mount: None
            for mount in profile.weapon_mounts
        }

        self.max_weapons = profile.weapon_slots
        self.speed = profile.speed


    @property
    def body(self):
        return self.locations[LocationType.BODY]
    
    @property
    def head(self):
        return self.locations[LocationType.HEAD]
    
    @property
    def legs(self):
        return self.locations[LocationType.LEGS]
    
    @property
    def destroyed(self):
        return self.body.destroyed
    

    def destroy_titan(self):
        for location in self.locations.values():
            location.hp = 0

    def equip_weapon(self, mount: WeaponMount, weapon: WeaponTemplate):
        if mount not in self.weapon_mounts:
            raise ValueError(
                f"{self.class_name} cannot use {mount.value}"
            )
        
        # handle this better by replacing the weapon?
        if self.weapon_mounts[mount] is not None:
            raise ValueError(
                f"{mount.value} already has a weapon"
            )
        
        self.weapon_mounts[mount] = weapon


    def take_damage(self, loc: Location):
        if not self.shields.collapsed:
            self.shields.absorb_hit()
        else:
            """take damage"""

    def repair(self):
        """conduct repairs on any broken systems"""
        """ e.g. weapons, shields offline, reactor vent, locomotors"""

    def end_turn_events(self):
        self.repair()
        self.reactor.cool_reactor()
        self.shields.repair()
        self.reactor.check_heat() # might go boom if too hot

