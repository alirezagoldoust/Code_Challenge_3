import json

class Customer:
    id_counter = 0 

    def __init__(self, name, phonenumber, address):
        self.id = Customer.id_counter
        Customer.id_counter += 1
        self.name = name
        self.__phonenumber = phonenumber
        self.address = address
        self.products = [] 

    def __str__(self):
        return f"Customer {self.name} has purchased: {self.products}"

    def buy_product(self, product, count_product):
        product_entry = {"product": product, "quantity": count_product}

        
        try:
            with open("store.json", "r") as stjson:
                data = json.load(stjson)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(product_entry)

       
        with open("store.json", "w") as stjson:
            json.dump(data, stjson, indent=4)

        self.products.append(product_entry)
        return f"Product {product} added to customer's purchase history."


class Seller:
    id_counter = 0

    def __init__(self, name, phonenumber, address):
        self.id = Seller.id_counter
        Seller.id_counter += 1
        self.name = name
        self.__phonenumber = phonenumber
        self.address = address
        self.products_for_sale = []  

    def __str__(self):
        return f"Seller {self.name} has products: {self.products_for_sale}"

    def product_for_sell(self, product):
        self.products_for_sale.append(product)
        try:
            with open("seller_store.json", "r") as selljson:
                data = json.load(selljson)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(product)
        with open("seller_store.json", "w") as selljson:
            json.dump(data, selljson, indent=4)

        return f"Product {product} added for sale."
