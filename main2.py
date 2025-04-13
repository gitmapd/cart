from collections import defaultdict
from datetime import datetime
from loader import load_items_from_file
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

   

inventory  = Inventory()

load_items_from_file("frutas.csv",inventory)

apple =inventory.get_item("F2")
print(apple)

