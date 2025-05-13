# Base class
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self.__strength_level = strength_level  # encapsulated attribute

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Super Power: {self.power}")

    def get_strength(self):
        return self.__strength_level

    def set_strength(self, new_strength):
        if new_strength > 0:
            self.__strength_level = new_strength
        else:
            print("Strength must be positive.")

    def action(self):
        print(f"{self.name} uses {self.power}!")
class FlyingHero(Superhero):
    def __init__(self, name, power, strength_level, altitude_limit):
        super().__init__(name, power, strength_level)
        self.altitude_limit = altitude_limit

    def action(self):
        print(f"{self.name} takes off and flies through the sky! ✈️")

    def fly_info(self):
        print(f"{self.name} can fly up to {self.altitude_limit} meters high.")
# Creating objects
hero1 = Superhero("ShadowStrike", "Invisibility", 85)
hero2 = FlyingHero("SkyBlazer", "Wind Blast", 95, 12000)

# Using methods
hero1.show_info()
hero1.action()
print("Strength level:", hero1.get_strength())

print("\n---\n")

hero2.show_info()
hero2.action()
hero2.fly_info()
