from dataclasses import dataclass
from position import Position
from faction import Faction


@dataclass
class BattlefieldEntity:
    name: str
    position: Position
    owner: Faction
    id: int | None = None
    visible: bool=True
    destructable: bool=True



    def __init__(self, name, owner, position):
        self.name = name
        self.position = position
        self.owner = owner
        self.id = 5
        self.visible = True
        self.destructable = True
