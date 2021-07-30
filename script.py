# Creating Businesses!
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# Creating the Franchises
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address
  
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if (time>=menu.start_time and time<=menu.end_time):
        available_menus.append(menu)
    return available_menus  

# Making the Menus
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{} menu available from {} to {}".format(self.name, self.start_time, self.end_time)

  def calculate_bill(self, purchased_items):
    tot = 0
    for item in purchased_items:
      if item in self.items:
        tot += self.items[item]
    return tot



brunch_menu = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
early_bird_menu = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinner_menu = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids_menu = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}


brunch = Menu("Brunch", brunch_menu, 11, 16)
early_bird = Menu("Early Bird", early_bird_menu, 15, 18)
dinner = Menu("Dinner", dinner_menu, 17, 23)
kids = Menu("Kids Menu", kids_menu, 11, 21)
arepas = Menu("Take a\' Arepa", arepas_menu, 10, 18)

# print(brunch)


bill1 = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
# print(bill1)
bill2 = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
# print(bill2)

menus = [brunch, early_bird, dinner, kids]


flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas]) 

#print(flagship_store.available_menus(12))
#print(flagship_store.available_menus(17))

basta = Business("Basta Fazoolin\' with my Heart", [flagship_store, new_installment])
arepa = Business("Take a\' Arepa", [arepas_place])
#print(arepa.franchises[0].menus[0])