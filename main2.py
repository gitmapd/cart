from collections import defaultdict
from datetime import datetime

class Item:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return (
            f"{self.nome} ({self.codigo}) - €{self.preco:.2f}"
        )

class Inventory:
    def __init__(self):
        self.items = {}  

    def add_item(self, codigo, nome, preco):
        self.items[codigo] = Item(codigo, nome, preco)
    def get_item(self, codigo):
        return self.items.get(codigo)


    def __str__(self):
        return f"{self.nome} - {self.descricao}"

inventory  = Inventory()

inventory.add_item("F1", "Maca", 1.00)

apple =inventory.get_item("F1")
print(apple)

