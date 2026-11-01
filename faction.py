from dataclasses import dataclass




@dataclass
class Faction:
    name: str


    def __init__(self, name):
        self.name = name
    