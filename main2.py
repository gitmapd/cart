from collections import defaultdict
from datetime import datetime
import rich
from rich import table, prompt
import datetime
from rich.progress import track
from rich.console import Console
from loader import load_items_from_file

console = Console()
class Item:
    def __init__(self, code, name, stock, price, category):
        self.code = code
        self.name = name
        self.stock = stock
        self.price = price
        self.category = category
    
    def __repr__(self):
        return f"({self.code}) {self.name} {self.stock} {float(self.price):.2f} {self.category}"

class Inventory:
    def __init__(self):
        self.items = {}  

    def add_item(self, code, name, price, stock, category):
        self.items[code] = Item(code, name, price, stock, category)
    def get_item(self, code):
        return self.items.get(code)

    def update_stock(self, code, quantity):
        if code in self.items:
            self.items[code].stock += quantity
            
    def update_price(self,code, price):
        if code in self.items:
            self.items[code].price = price
    
    def is_in_stock(self, code, quantity):
        return code in self.items and self.items[code].stock >= quantity
    
    def reduce_stock(self, code, quantity):
        if self.is_in_stock(code,quantity):
            self.items[code].stock -= quantity
            return True
        return False
   
class Category:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.description}"

class ShoppingCart:
    def __init__(self):
        self.items = defaultdict(int)
    def add_item(self,item_code, quantity=1):
        self.items[item_code] += quantity
    def remove_item(self,item_code, quantity=1):
        if item_code in self.items:
            self.items[item_code] -= quantity
            if self.items[item_code] <= 0:
                del self.items[item_code]
    def __repr__(self):
        return f"Cart: {dict(self.items)}"
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.cart = ShoppingCart()
        self.purchase_history = []

    def add_to_cart(self, item_code, quantity=1):
        self.cart.add_item(item_code, quantity)


    def checkout(self):
        timestamp = datetime.now()
        purchased_items = self.cart.get_items()
        self.purchase_history.append((timestamp, purchased_items))
        self.cart.clear_cart()
        return timestamp, purchased_items

    def __repr__(self):
        return f"{self.name} (ID: {self.customer_id})"
class Sales:
    def __init__(self):
        self.customers = {}
        self.sales_log = []

    def add_customer(self, customer_id, name):
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id, name)
    def get_customer(self, customer_id):
        return self.customers.get(customer_id)
    
    def record_sale(self, customer_id):
        customer = self.get_customer(customer_id)
        if customer:
            timestamp, items = customer.checkout()
            self.sales_log.append((customer_id, timestamp, items))
            return timestamp, items
        return None
    def sales_by_customer(self, customer_id):
        return [sale for sale in self.sales_log if sale[0] == customer_id]
    def all_sales(self):
        return self.sales_log
    def __repr__(self):
        return f"Sales Log: {self.sales_log}"
def main():
    inventory  = Inventory()
    load_items_from_file("frutas.csv",inventory)
    
    #prod_table = table.Table(show_header=True, header_style="bold magenta", expand=True, highlight=True)
    #prod_table.add_column("Código", justify="center")
    #prod_table.add_column("name", justify="center")
    #for k,v in track(inventory.items.items(), description="A Processar..."):
    #    prod_table.add_row(str(k)[:5])

    #console.rule("Frutas", style="bold yellow")
    #console.print(prod_table)
    inventory.add_item("F44","Tangerina",20,2,"frutas")
    #apple2=inventory.get_item("F44")
    #inventory.update_price("F2",30)
    #apple2 =inventory.get_item("F2")
    #inventory.reduce_stock("F2",3)
    #inventory.reduce_stock("F44",10)
    #apple2=inventory.get_item("F44")
    #print(apple2)
    sales = Sales()
    sales.add_customer(101, "Alice")
    sales.get_customer(101).add_to_cart("F44", 2)
    sales.get_customer(101).add_to_cart("F43", 1)
# Checkout and record the sale
    sales.record_sale("F43")
    print(sales.sales_by_customer(101))
    print(sales.all_sales())

if __name__ == '__main__':
        main()