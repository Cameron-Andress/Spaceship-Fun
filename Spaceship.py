class Spaceship:
    
    def __init__(self, name, speed, fuel):
        self.name = name          # The name of the spaceship
        self.speed = speed        # Speed of the spaceship
        self.fuel = fuel          # Current fuel level

    def fly(self, distance):
        """Simulates flying the spaceship a certain distance."""
        fuel_needed = distance * 0.1  # Assume 0.1 fuel units per distance
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print(f"{self.name} flew {distance} units!")
        else:
            print(f"{self.name} doesn't have enough fuel to fly!")

# Create an instance of Spaceship
spaceship = Spaceship("Apollo", 500, 100)

# Call the fly method on the instance
spaceship.fly(200)
