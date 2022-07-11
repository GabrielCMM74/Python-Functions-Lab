class Dog():

  next_id = 1

  def __init__(self, name, age = 0):
    self.name = name
    self.age = age
    self.id = Dog.next_id
    Dog.next_id += 1

  def bark(self):
    print(f'{self.name} says woof!')

  def __str__(self):
    return f'Dog ({self.id}) named {self.name} is {self.age} years old'

  @classmethod
  def get_total_dogs(cls):
    # cls represents the Dog class
    return cls.next_id - 1


spot = Dog('Spot', 8)
print(spot) # -> similar to <__main__.Dog object at 0x7f27bad2c208>
# print the name and age attributes of the spot object
print(spot.name, spot.age) # -> Spot 8
# invoke the spot object's bark instance method
spot.bark() # -> Spot says woof!
pup = Dog('Lassie')
print(pup.name, pup.age) # -> Lassie 0
print(Dog.get_total_dogs())


# Pass in superclass as argument
class ShowDog(Dog):
  # Add additional parameters AFTER those in the superclass
  def __init__(self, name, age = 0, total_earnings = 0):
    # Always call the superclass's __init__ first
    Dog.__init__(self, name, age)
    # Now add any new attributes
    self.total_earnings = total_earnings
  
  # Add additional methods
  def add_prize_money(self, amount):
    self.total_earnings += amount

winky = ShowDog('Winky', 3, 1000)
print(winky) # Yay, inherited the overriden __str__
winky.bark() # Yay, inherited the bark method
print(winky.total_earnings) # -> 1000
winky.add_prize_money(500) # New method that 'Dogs' don't have
print(winky.total_earnings) # -> 1500



class Vehicle():

    next_id = 1

    def __init__(self, vin, make, model, running = False):
        self.vin = vin
        self.make = make
        self.model = model
        self.running = running
        self.id = Vehicle.next_id
        Vehicle.next_id += 1

    def start(self):
        self.running = True
        print(f"The car {self.id} has this vin {self.vin}, this make {self.make}, this model {self.model}, and running is {self.running}   ")

    def stop(self):
        self.running = False
        print(f" The car is {self.running} running")

    def __str__(self):
        return f'My Vehicle {self.id} is {self.vin}, make is {self.make}, model is {self.model}, car is running {self.running}'

    @classmethod
    def get_total_cars(cls):
        return cls.next_id - 1


car = Vehicle('TS123', 'Tesla', 'Model S')
print(car.running)
print(car.vin,car.make,car.model)
print(car)
car.start()
print(car.running)
plane = Vehicle('X99Y', 'Boeing', '747-B')
print(plane.vin, plane.make, plane.model)
print(Vehicle.get_total_cars())


