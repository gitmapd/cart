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
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
    
    def __repr__(self):
        return (
            f"({self.codigo}) {self.nome} - €{self.preco:.2f}"
        )

class Inventory:
    def __init__(self):
        self.items = {}  

    def add_item(self, codigo, nome, preco):
        self.items[codigo] = Item(codigo, nome, preco)
    def get_item(self, codigo):
        return self.items.get(codigo)


    def __repr__(self):
        return f"{self.nome} - {self.descricao}"

   


def main():
    inventory  = Inventory()
    load_items_from_file("frutas.csv",inventory)
    
    prod_table = table.Table(show_header=True, header_style="bold magenta", expand=True, highlight=True)
    prod_table.add_column("Código", justify="center")
    prod_table.add_column("Nome", justify="center")
    for k,v in track(inventory.items.items(), description="A Processar..."):
            print(v)
            #prod_table.add_row('Nome',it)

    console.rule("Boletim", style="bold yellow")
    console.print(prod_table)
    apple =inventory.get_item("F2")
    print(apple)

if __name__ == '__main__':
        main()