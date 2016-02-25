
class Bicycle(object):
    def __init__(self, model = 'Trek', weight = 10):
        self.model_name = model
        self.weight = weight

    def cost(self):
        return self.weight * 20

class BicycleShop(object):

    def __init__(self, name = "Bill's Bikes", inventory = []):
        self.name = name
        self.inventory = inventory

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
        return 0.20 * cost_of_goods

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

    def bike_in_budget(self, bike_model):
        return self.budget >= bike_model.cost()

    def purchase_bike(self, bike_model):
        if bike_in_budget(bike_model):
            self.budget -= bike_model.cost()
            self.bicycles.append(bike_model)
