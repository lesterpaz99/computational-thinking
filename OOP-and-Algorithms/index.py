class Hotel:
  def __init__(self, max_number_guests, parking_spaces):
    self.max_number_guests = max_number_guests
    self.parking_spaces = parking_spaces
    self.guests = 0
    
  def add_guests(self, amount):
    self.guests += amount

  def checkout(self, amount_of_guests):
    self.guests -= amount_of_guests

  def total_occupation(self):
    return self.guests


myHotel = Hotel(50, 20)
myHotel.add_guests(5)
print(myHotel.guests)
print(myHotel.total_occupation())