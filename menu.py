import hashlib
from product import ProductManagement
from users import Seller
class Account_manger:
    def __init__(self):
        self._list_of_seller = []
        self._list_of_costumer = []
        self._list_of_product = []

    def add_user(self, username:str, password:str, role: str):
        new_user = User(username= username, password=password)
        self.__user_list.append(new_user)
    
        if role == "costumer" :
            self._list_of_costumer.append(new_user)
        elif role == "seller":
           self._list_of_seller.append(new_user)    
        else:
            raise ValueError("505")
    
    def signup(self, username, password):
        new_user = self.add_user(username, password)
        return new_user
            
    def login(self, username, password):
        for user in self.__user_list:
            if user.get_username() == username and user.get_password() == password:
                return user
            else:
            
                return None

class Menu_list :
    def __init__(self):
        self.account_manager = Account_manger()

        self.__active_user =  None
    
    def _list_of_product(self):
        product_list = ProductManagement.get_product_list()
        counter = 1
        for product in product_list:
            print(f"{counter}: {product}")
            counter += 1
    
    def menu(self):
        while self.__active_user == None:
            print("1.login")
            print("2.signup")
            print("what is your choice? ")
            choice = int(input())
            if choice == 1:
                user_name = input("what is your username? ")
                pass_word = input("what is your password? ")
                role = input("what is your role?")
                user = self.account_manager.login(user_name, pass_word, role)
                if user != None:
                    self.__active_user = user
            elif choice == 2 :
                user_name = input("what is your username? ")
                pass_word = input("what is your password? ")
                user = self.account_manager.signup(user_name, pass_word)
                if user != None:
                    self.__active_user = user
        if self.__active_user != None and self.__active_user._role == "customer":
            print("1. list of product")
            print("2. search your product")
            print("3. buy your product")
            print("4. list of orders")
            choice = int(input())

            if choice == 1:
                self._list_of_product()
                
            elif choice == 2 :
                self.add_to_order_list()

            elif choice == 3:
                self.add_to_order_list()

            elif choice == 4:  
                pass
                

        elif self.__active_user != None and self.__active_user._role == "seller":
            print("1.list of product")
            print("2.add product")
            print("3.list of orders")
            print("4.list of costumers")
            choice = int(input())
            if choice == 1:
                s_products = Seller.product_for_sell()
                counter = 1
                for product in s_products:
                    print(f"{counter}: {product}")
                    counter += 1
            elif choice == 2:

            

                     

    def login(self):
        username = input()
        password = input()
        self.__active_user = self.account_manager.login(username, password)
        if not self.__active_user:
            print("wrong username")


class User:
    id = 1
    def __init__(self,username: str , password: int, role: str):
        self._username = username
        self._password = User.hash_password(password)
        self._role = role

        User.id += 1 

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def get_username(self):
        return self._username   

    def set_username(self, username: str):
        self._username = username

    def get_password(self):
        return self._password
    
    def set_password(self, password: int ):
        self._password = password

    def get_role(self):
        return self._role
    
    def set_role(self,role: str):
        self._role = role


class Customer:
    def __init__(self, username, password):
        super().__init__(username , password)
        self._order_list = []

    def ls(self, list_of_product):
        return list_of_product
        
    def search(self, list_of_product, desired_product):
        for i in list_of_product:
            if list_of_product[i] == desired_product:
                return desired_product
            else:
                return "404"

    def ls_order(self):
        return self._order_list

    def add_to_order_list(self, bought_product, list_of_product):
        for i in list_of_product:
            if list_of_product[i] == bought_product:
                self._order_list.append(bought_product)
            else:
                return "404"

    def remove_from_order_list(self, product):
        for i in self._order_list:
            if product == self._order_list[i]:
                self._order_list.remove(product)
            else:
                return "404"
            
class Seller():
    def __init__(self, username, password):
        super().__init__(username , password)
        self._list_of_product = []

    def add_product(self, product):
        self._list_of_product.append(product)
        Account_manger.self._list_of_product.append(product)
