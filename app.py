class Product:
    def __init__(self, name, price, deal_price, rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating
        self.you_save=price - deal_price
        
    def display_product(self):
        print(f"Product Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Deal Price: {self.deal_price}")
        print(f"Rating: {self.rating}")
        print(f"You Save: {self.you_save}")
        
    def get_deal_price(self):
        return self.deal_price
    def get_price(self):
        return self.price
        
    def update_deal_price(self, new_deal_price):
        self.deal_price=new_deal_price
    
    def update_price(self, new_price):
        self.price=new_price

class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, rating, warrenty_in_months):
        super().__init__(name, price, deal_price, rating)
        self.warrenty_in_months=warrenty_in_months
    
    def display_product(self):
        super().display_product()
        print(f"Warrenty In Months: {self.warrenty_in_months} months")
        
class GroceryItem(Product):
    def __init__(self, name, price, deal_price, rating, expiry_date):
        super().__init__(name, price, deal_price, rating)
        self.expiry_date=expiry_date
    
    def display_product(self):
        super().display_product()
        print(f"expiry_date: {self.expiry_date} days")

class Laptop(ElectronicItem):
    def __init__(self, name, price, deal_price, rating, warrenty_in_months, ram, storage):
        super().__init__(name, price, deal_price, rating, warrenty_in_months)
        self.ram=ram
        self.storage=storage
    
    def display_product(self):
        super().display_product()
        print(f"Ram: {self.ram}")
        print(f"Storage: {self.storage}")

class WashingMachine(ElectronicItem):
    def __init__(self, name, price, deal_price, rating, warrenty_in_months, load_type, capacity):
        super().__init__(name, price, deal_price, rating, warrenty_in_months)
        self.load_type=load_type
        self.capacity=capacity

    def display_product(self):
        super().display_product()
        print(f"Load Type: {self.load_type}")
        print(f"Capacity: {self.capacity}")

class Order:
    delivery_charges = {
        "Normal": 0,
        "Prime": 100
    }
    
    def __init__(self, delivery_method, delivery_address):
        self.item_in_cart=[]
        self.delivery_method=delivery_method
        self.delivery_address=delivery_address
    
    def add_item(self, product, quantity):
        item = (product, quantity)
        self.item_in_cart.append(item)
    
    def display_order_details(self):
        print(f"Delivery Method ------------------ {self.delivery_method}")
        print(f"Delivery Address ----------------- {self.delivery_address}")
        print("Products")
        print("---------------------------------------------------------------")
        for product, quantity in self.item_in_cart:
            product.display_product()
            print(f"Quantity {quantity}")
            print("")
        print("---------------------------------------------------------------")
        total_bill=self.get_total_bill()
        total_price=self.get_total_price()
        order_delivery_charges = Order.delivery_charges[self.delivery_method]
        print(f"Total Price ---------------------- {total_price}")
        print(f"Total Deal Price ----------------- {total_bill}")
        print(f"Total You Save ------------------- {total_price - total_bill}")
        print(f"Delivery Charges ----------------- {order_delivery_charges}")
        print("====================================================================")
        print(f"Total Bill ----------------------- {total_bill + order_delivery_charges}")
        print("=====================================================================")
        
    def get_total_bill(self):
        total_bill=0
        for product, quantity in self.item_in_cart:
            total_bill = total_bill + product.get_deal_price()*quantity
        return total_bill
        
    @classmethod
    def update_delivery_charges(cls, delivery_method, charges):
        cls.delivery_charges[delivery_method] = charges
        
    def get_total_price(self):
        total_price=0
        for product, quantity in self.item_in_cart:
            total_price=total_price+product.get_price()*quantity
        return total_price

laptop=Laptop("Hp palivilion 15", 70000, 65000, 4.5, 12, "12GB", "1TB")
w1=WashingMachine("lg 10g", 60000, 45000, 4.5, 48, "Top load", "8Kg")

my_order=Order("Prime", "Hyderabd-KPHP-JNTU")
my_order.add_item(laptop, 2)
my_order.add_item(w1, 1)
my_order.display_order_details()


 