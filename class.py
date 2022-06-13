class Car(object):
  def __init__(self, model, color, company, speed_limit):
    self.model = model
    self.color = color
    self.company = company
    self.speed_limit = speed_limit

  def start(self):
    print("Started")

  def stop(self):
    print("Stopped")

  def accelerate(self):
    print("Accelerating")

  def change_gear(self):
    print("Changing Gear")
audi = Car("A6", "Blue", "Audi", "200")
print(audi.start())

