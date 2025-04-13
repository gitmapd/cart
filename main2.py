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
    apple2=inventory.get_item("F44")
    print(apple2)

if __name__ == '__main__':
        main()