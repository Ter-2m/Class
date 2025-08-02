class Superhero:
    def __init__(self, name, secret_identity, powers):
        """
        Initializes a Superhero object.

        Args:
            name (str): The superhero's name.
            secret_identity (str): The superhero's secret identity.
            powers (list): A list of the superhero's powers.
        """
        self.name = name
        self.__secret_identity = secret_identity  # Encapsulated attribute
        self.powers = powers

    def display_info(self):
        """
        Displays basic information about the superhero.
        """
        print(f"Superhero Name: {self.name}")
        print(f"Powers: {', '.join(self.powers)}")

    def use_power(self, power_name):
        """
        Simulates the superhero using a specific power.
        """
        if power_name in self.powers:
            print(f"{self.name} uses {power_name}!")
        else:
            print(f"{self.name} does not possess {power_name}.")

    def reveal_secret_identity(self):
        """
        Reveals the superhero's secret identity (demonstrates encapsulation access).
        """
        print(f"Secret Identity: {self.__secret_identity}")


class FlyingSuperhero(Superhero):
    def __init__(self, name, secret_identity, powers, flight_speed):
        """
        Initializes a FlyingSuperhero object, inheriting from Superhero.

        Args:
            name (str): The superhero's name.
            secret_identity (str): The superhero's secret identity.
            powers (list): A list of the superhero's powers.
            flight_speed (int): The superhero's flight speed in mph.
        """
        super().__init__(name, secret_identity, powers)
        self.flight_speed = flight_speed

    def fly(self):
        """
        Simulates the flying superhero taking flight.
        """
        print(f"{self.name} takes to the skies at {self.flight_speed} mph!")

    def display_info(self):
        """
        Overrides the display_info method to include flight speed (polymorphism).
        """
        super().display_info()
        print(f"Flight Speed: {self.flight_speed} mph")


# Create instances of the classes
superman = FlyingSuperhero("Superman", "Clark Kent", ["Flight", "Super Strength", "Heat Vision"], 800)
batman = Superhero("Batman", "Bruce Wayne", ["Intelligence", "Martial Arts", "Gadgets"])

# Demonstrate attributes and methods
print("--- Superman's Info ---")
superman.display_info()
superman.fly()
superman.use_power("Heat Vision")
superman.reveal_secret_identity()

print("\n--- Batman's Info ---")
batman.display_info()
batman.use_power("Martial Arts")
batman.reveal_secret_identity()