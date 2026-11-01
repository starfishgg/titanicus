from entity import BattlefieldEntity
from titan import Titan
from faction import Faction
from entity import BattlefieldEntity



class Battlefield:
    entities: list[BattlefieldEntity]
    battlefieldSizeX: int=150
    battlefieldSizeY: int=100

    def __init__(self):
        self.entities = []

    def add_entity(self, entity: BattlefieldEntity):
        self.entities.append(entity)

    def remove_entity(self, entity:BattlefieldEntity):
        self.entities.remove(entity)

    def get_entity_by_name(self, name):
        for entity in self.entities:
            if entity.name == name:
                return entity
            
        return None


    def walk_entity(entity: BattlefieldEntity, new_position):
        """is the destination on the map?"""
        """is the destination blocked, e.g. by another titan?"""
        """is the movement path blocked?"""
        entity.position.x = new_position.x
        entity.position.y = new_position.y
        entity.position.facing = new_position.facing

    def get_titans(self):
        return [
            entity
            for entity in self.entities
            if isinstance(entity, Titan)
        ]
    

    def get_titans_by_owner(self, owner):
        return [
            entity
            for entity in self.entities
            if isinstance(entity, Titan)
            and entity.owner == owner
        ]
    
    def get_enemies(self, owner):
        return [
            entity
            for entity in self.entities
            if entity.owner is not None
            and entity.owner != owner
        ]
    
    def get_neutrals(self):
        return [
            entity
            for entity in self.entities
            if entity.owner is None
        ]
    

    def distance_between(self, entity1: BattlefieldEntity, entity2: BattlefieldEntity):
        return entity1.position.distance_to(entity2.position)
        



class Game:
    battlefield: Battlefield
    factionA: Faction
    factionB: Faction
    # factionN: Faction

    def __init__(self):
        self.battlefield = Battlefield()
        self.factionA = Faction("Legio Tempestus")
        self.factionB = Faction("Legio Mortis")
        #self.factionN = Faction("Neutral")

    """control phases here: strategy, movement, combat, damage control"""
