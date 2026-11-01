from dataclasses import dataclass
from enum import Enum, auto



class WeaponTrait(Enum):
    SHIELDBANE = auto()
    ARMOURBANE= auto()
    ORDNANCE = auto()
    BLAST = auto()
    RAPID = auto()
    MELTA = auto()
    HEAT = auto()
    LIMITED_AMMO = auto()
    CRITICAL = auto()
    QUAKE = auto()


class WeaponClass(Enum):
    NONE = "none",
    ARM = "arm",
    CARAPACE = "carapace"


class WeaponArc(Enum):
    FRONT = "front",
    LEFT = "left",
    RIGHT = "right",
    REAR = "rear"




@dataclass(frozen=True)
class WeaponTemplate:
    name: str
    range: int
    attacks: int
    accuracy: int
    strength: int
    armour_penetration: int
    traits: tuple[WeaponTrait, ...] = ()
    arc: WeaponArc = WeaponArc.FRONT
    heat: int = 0




TURBO_LASER = WeaponTemplate(
    name="Turbo Laser Destructor",
    range=96,
    attacks=3,
    accuracy=4,
    strength=10,
    armour_penetration=3,
    traits=(WeaponTrait.SHIELDBANE,),
    heat=1,
)


MEGA_BOLTER = WeaponTemplate(
    name="Vulcan Mega Bolter",
    range=30,
    attacks=8,
    accuracy=4,
    strength=6,
    armour_penetration=0,
    traits=(WeaponTrait.RAPID,),
)


GATLING_BLASTER = WeaponTemplate(
    name="Gatling Blaster",
    range=20,
    attacks=6,
    accuracy=4,
    strength=5,
    armour_penetration=0,
    traits=(WeaponTrait.RAPID,),
)

VOLCANO_CANNON = WeaponTemplate(
    name="Volcano Cannon",
    range=40,
    attacks=2,
    accuracy=5,
    strength=10,
    armour_penetration=0,
    traits=(WeaponTrait.ARMOURBANE,),
    heat=2,
)


MISSILE_LAUNCHER = WeaponTemplate(
    name="Apocalypse Missile Launcher",
    range=40,
    attacks=10,
    accuracy=5,
    strength=4,
    armour_penetration=0,
    traits=(WeaponTrait.ORDNANCE,),
)

LASER_BLASTER = WeaponTemplate(
    name="Laser Blaster", 
    range=24,
    attacks=5,
    accuracy=3,
    strength=8,
    armour_penetration=0,
    traits=(),
)

MELTA_CANNON = WeaponTemplate(
    name="Melta Cannon",
    range=8,
    attacks=2,
    accuracy=2,
    strength=11,
    armour_penetration=0,
    traits=(WeaponTrait.MELTA,),
)

QUAKE_CANNON = WeaponTemplate(
    name="More Quake Cannon",
    range=36,
    attacks=1,
    accuracy=5,
    strength=9,
    armour_penetration=0,
    traits=(WeaponTrait.QUAKE,),
)

INFERNO_GUN = WeaponTemplate(
    name="Inferno Gun",
    range=8,
    attacks=4,
    accuracy=2,
    strength=7,
    armour_penetration=0,
    traits=(WeaponTrait.HEAT,),
)