class Store:
    def __init__(self, name, list_of_products = []):
        self.name = name
        self.list_of_products = list_of_products

    def add_product(self, new_product):
        self.list_of_products.append(new_product)

    def sell_product(self, id):
        print(f"{self.list_of_products[id]} has been sold!")
        self.list_of_products.remove(list_of_products[id])

    def inflation(self, percent_increase):
        for x in list_of_products:
            self.x.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for x in list_of_products:
            self.x.update_price(percent_increase, False)
        return self



class Products:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if(is_increased):
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)
    
    def print_info(self):
        print(f"Product Name: {self.name} Category: {self.category} Price: ${self.price}")



walmart = Store("Wally")
tide = Products("Tide", 8.95, "Laundry Supplies")
tp = Products("Charmin Ultra", 4.95, "Bathroom Supplies")
toothpaste = Products("Crest", 5.05, "Dental Hygiene")


print(walmart.list_of_products)
walmart.add_product(tide)
walmart.add_product(tp)
walmart.add_product(toothpaste)


print(walmart.list_of_products[0].name)

walmart.sell_product(0)
print(walmart.list_of_products[0].name)


