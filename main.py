from titan import Titan, WeaponMount
from weapon import WeaponTemplate, TURBO_LASER, MEGA_BOLTER
from building import Building
from position import Position
from game import Game
from faction import Faction



def report_titan_status(titan: Titan):
    print(f"Titan Name: {titan.name}")
    print(f"Titan Class: {titan.class_name}")
    print(f"Speed: {titan.speed}")
    print(f"Void Shields: {titan.shields.current_voids}")

    print("\nLocations:")
    for location in titan.locations.values():
        print(f"{location.type.name.capitalize()}: Armour={location.armour}, HP={location.hp}")

    print("\nReactor:")
    print(f"Max Heat: {titan.reactor.max_heat}")
    print(f"Current Heat: {titan.reactor.current_heat}")
    print(f"Heat %: {titan.reactor.level}")


def fire_gun(titan: Titan):
    titan.reactor.add_pending_heat(2)
    print(f"Generated {titan.reactor.get_pending_heat()} pending heat from firing volcano cannon.")


def apply_heat(titan: Titan):
    titan.reactor.apply_pending_heat()
    print(f"Applied pending heat. Current Heat: {titan.reactor.current_heat}. Pending Heat: {titan.reactor.pending_heat}.")


def equip_weapons(titan: Titan):
    titan.equip_weapon(
        WeaponMount.LEFT_ARM,
        TURBO_LASER
    )

    titan.equip_weapon(
        WeaponMount.RIGHT_ARM,
        MEGA_BOLTER
    )


def weapons_report(titan: Titan):
    print(f"{titan.name} weapon loadout:")
    for mount, weapon in titan.weapon_mounts.items():
        if weapon:
            print(f"  {mount.value}: {weapon.name}")
        else:
            print(f"  {mount.value}: Empty")


def building_report(building: Building):
    # Basic information
    print("Name:", building.name)

    # Position
    print("Position:")
    print("  X:", building.position.x)
    print("  Y:", building.position.y)
    print("  Facing:", building.position.facing)

    # Building stats
    print("Armour:", building.armour)
    print("Structure:", building.hp)

    # Test destroyed property
    print("Destroyed:", building.destroyed)

def owner_check(g: Game):
    print("Titans on the battlefield:")
    titans = g.battlefield.get_titans()
    for titan in titans:
        print(f"- {titan.name} ({titan.class_name}), {titan.owner.name}")


def enemy_check(g: Game):
    print(f"Enemies of {g.factionA.name}:")
    enemies = g.battlefield.get_enemies(g.factionA)
    for enemy in enemies:
        print(f"- {enemy.name} ({enemy.class_name}), {enemy.owner.name}")


def neutral_check(g: Game):
    print("Neutral List:")
    neutrals = g.battlefield.get_neutrals()
    for n in neutrals:
        print(f"- {n.name}")


def main():
    g = Game()

    # Create a warlord titan
    my_titan = Titan(name="Stormherald", titan_type="warlord", owner=Faction("Legio Tempestus"), position=Position(x=10, y=5, facing=0.0))

    enemy_titan = Titan(name="Hell's Wrath", titan_type="reaver", owner=Faction("Legio Mortis"), position=Position(x=50, y=50, facing=270.0))

    # Create a building
    my_building = Building(name="Aquila Manufactorum", owner=None, position=Position(x=20, y=15, facing=180.0), armour=5, hp=20)

    g.battlefield.entities.append(my_titan)
    g.battlefield.entities.append(my_building)
    g.battlefield.entities.append(enemy_titan)

    my_titan = g.battlefield.get_entity_by_name("Stormherald")
    my_building = g.battlefield.get_entity_by_name("Aquila Manufactorum")

    report_titan_status(my_titan)
    equip_weapons(my_titan)
    weapons_report(my_titan)

    # Simulate firing a volcano cannon
    fire_gun(my_titan)

    # Apply pending heat
    apply_heat(my_titan)

    building_report(my_building)
    
    owner_check(g)
    enemy_check(g)
    neutral_check(g)





if __name__ == "__main__":
    main()
