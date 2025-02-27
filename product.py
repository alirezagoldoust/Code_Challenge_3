#classes : product: physical, digital | order 
import os
import json
products_data = "products_data.json"
class ProductManagement:
    def __init__(self):
        self.product_list = []

    def load(self):
        if os.path.exists(products_data):
            with open(products_data,"r") as f:
                self.product_list = json.load(f)
        for i in range(len(self.product_list)):
            if self.product_list[i]["type"] == "physical":
                self.product_list[i] = PhysicalProduct(
                    self.product_list[i]["name"],
                    self.product_list[i]["category"],
                    self.product_list[i]["price"],
                    self.product_list[i]["stock"],
                    self.product_list[i]["weight"],
                    self.product_list[i]["seller"],
                )
            elif self.product_list[i]["type"] == "digital":
                self.product_list[i] = DigitalProduct(
                    self.product_list[i]["name"],
                    self.product_list[i]["category"],
                    self.product_list[i]["price"],
                    self.product_list[i]["download_link"],
                    self.product_list[i]["seller"],
                )
                
    def add_product(self, product):
        self.product_list.append(product)
        list_of_product_dicts = [p.to_dict() for p in self.product_list]
        with open(products_data, "w") as f:
            json.dump(list_of_product_dicts, f, indent=4)
            
    def get_product_list(self):
        return self.product_list
    
    def search_by_name(self,search_name):
        for item in self.get_product_list:
            if item["name"] == search_name:
                return item
            
class Product:
    id = 0
    def __init__(self, name, category, price, seller):
        Product.id += 1
        self.id = Product.id
        self.name = name
        self.price = price
        self.category = category
        self.seller = seller
        
    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "seller": self.seller,
            "type": self.type
        }
        
class PhysicalProduct(Product):
    def __init__(self, name, category, price, stock, weight, seller):
        super().__init__(name, category, price,seller)
        self.weight = weight
        self.stock = stock
        self.type = "physical"
    def to_dict(self):
        ret = super().to_dict()
        ret.update(
        {
            "stock":self.stock,
            "weight":self.weight,
            "type": self.type
        })
        return(ret)
class DigitalProduct(Product):
    def __init__(self, name, category, price, download_link, seller):
        super().__init__(name, category, price)
        self.download_link = download_link
        self.type = "digital"
    def to_dict(self):
        ret = super().to_dict()
        ret.update(
        {
            "download_link":self.download_link
        })
        return(ret)

# p1 = Product(1,"ali","a",100)
manage = ProductManagement()
manage.load()
p2 = PhysicalProduct("ali","name", 2000, 2,10,"javad")
ProductManagement().add_product(p2)
