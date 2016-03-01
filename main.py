from bicycles import Bicycle, BicycleShop, Customer

if __name__ == '__main__':
    bike1 = Bicycle()
    huffy = Bicycle("Huffy", 30)
    speedster = Bicycle("Speedster", 5)
    shwin = Bicycle("Shwin", 20)

    bike1.cost()

    bills  = BicycleShop("Robert's Bikes", [bike1, huffy, speedster, shwin, huffy, bike1])

    print(bills.inventory_cost())
    print(bills.profit_or_loss())

    james = Customer("James", 200)
    edward = Customer("Eddy", 500)
    richie = Customer("Rich", 1000)

    customers = [james, edward, richie]

    print("-----------")
    customer_list = list(map((lambda customer: customer.name), customers)) ##is there a cleaner way to iterate and map over just the names?
    ## or customer_list = [customer.name for customer in customers]
    # print(customer_list)
    # print("customers are : {}".format(customer_list)
    bikes_in_customer_budget = {}

    for customer in customers:
        in_customer_budget = []
        for bike in bills.inventory:
            if customer.bike_in_budget(bike):
                in_customer_budget.append(bike)
        bikes_in_customer_budget[customer] = in_customer_budget

    for customer, bikes in bikes_in_customer_budget.items():
        bike_list = list(map((lambda bicycle: bicycle.model_name), bikes))
        print("{} can afford: {}".format(customer.name, bike_list))
