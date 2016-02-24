
class Bicycle(object):
    def __init__(self, model = 'Trek', weight = 10):
        self.model_name = model
        self.weight = weight

    def cost(self):
        return self.weight * 20

class BicycleShop(object):

    def __init__(self, name = "Bill's Bikes"):
        self.name = name
        self.inventory = []

    def add_to_inventory(self, bicycle_model = Bicycle()):
        self.inventory.append(bicycle_model)

    def sell_bicycle(self, bicycle_model = "Trek"):
        if bicycle_model in self.inventory:
            self.revenue += bicycle_model.cost()
            self.inventory.remove(bicycle_model)


    def inventory_cost(self):
        cost = 0
        for item in self.inventory:
            cost += item.cost()

        return cost

    def margin(self):
        cost_of_goods = self.inventory_cost()
        return 0.10 * cost_of_goods

    def profit_or_loss(self, bicycle_model = "Trek"):
        cost_of_sale = 100
        units = len(self.inventory)
        for i in self.inventory:
            self.sell_bicycle(bicycle_model)
        return self.margin() - (units * cost_of_sale)

class Customer(object):
    def __init__(self, name, budget = 300):
        self.name = name
        self.budget = budget
        self.bicycles = []

    def purchase_bike(self, bike_model):
        if self.budget > bike_model.cost():
            self.budget -= bike_model.cost()
            self.bicycles.append(bike_model)




b = Bicycle()

b.cost

# print(b.weight)

bills  = BicycleShop()

bills.add_to_inventory(Bicycle("Shwin", 20))

bills.add_to_inventory()

print(bills.inventory)
print(bills.inventory_cost())

print(bills.profit_or_loss())