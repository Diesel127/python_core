class Character:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.hp = self.base_hp * level
        self.attack_power = self.base_attack_power * level

    def attack(self, *, target: "Character") -> None:
        target.got_damage(damage=self.attack_power)

    def got_damage(self, *, damage: int) -> None:
        damage = damage * (100 - self.defence) / 100
        damage = round(damage)
        self.hp -= damage

    def hp_percent(self) -> float:
        return 100 * self.hp / self.max_hp

    @property
    def max_hp(self) -> int:
        return self.level * self.base_hp

    @property
    def defence(self) -> int:
        defence = self.base_defence * self.level
        return defence

    def is_alive(self) -> bool:
        return self.hp > 0

    def __str__(self) -> str:
        return f"{self.character_name} ({self.hp} hp)"

class Ork(Character):
    base_hp = 100
    base_attack_power = 10
    character_name = "Ork"
    base_defence = 15

    @property
    def defence(self) -> int:
        defence = super().defence
        if self.hp < 50:
            defence *= 3
        return defence

class Elf(Character):
    base_hp = 50
    base_attack_power = 15
    character_name = "Elf"
    base_defence = 10

    def attack(self, *, target: "Character") -> None:
        damage = self.attack_power
        if target.hp_percent() < 30:
            damage *= 3
        target.got_damage(damage=damage)

def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        print(f"{character_1} attacks {character_2} with {character_1.defence} defence")
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)
            print(f"{character_2} attacks {character_1} with {character_2.attack_power} attack_power")
    print(f"{character_1} is alive: {character_1.is_alive()}")
    print(f"{character_2} is alive: {character_2.is_alive()}")

ork = Ork(level=1)
elf = Elf(level=1)
fight(character_1=ork, character_2=elf)