class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def take_damage(self, damage: int) -> None:
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                if self in Animal.alive:
                    Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = True

class Carnivore(Animal):
    def bite(self, target: Herbivore) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.take_damage(100)
