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
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
    
    def __repr__(self):
        return (
            f"({self.code}) {self.name} - €{self.price:.2f}"
        )

class Inventory:
    def __init__(self):
        self.items = {}  

    def add_item(self, code, name, price):
        self.items[code] = Item(code, name, price)
    def get_item(self, code):
        return self.items.get(code)


    def __repr__(self):
        return f"{self.name} - {self.description}"

   


def main():
    inventory  = Inventory()
    load_items_from_file("frutas.csv",inventory)
    
    prod_table = table.Table(show_header=True, header_style="bold magenta", expand=True, highlight=True)
    prod_table.add_column("Código", justify="center")
    prod_table.add_column("name", justify="center")
    for k,v in track(inventory.items.items(), description="A Processar..."):
            print(v)
            #prod_table.add_row('name',it)

    console.rule("Boletim", style="bold yellow")
    console.print(prod_table)
    apple =inventory.get_item("F2")
    print(apple)

if __name__ == '__main__':
        main()