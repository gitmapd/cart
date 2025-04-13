from dataclasses import dataclass, field
import rich
from rich import table, prompt
import datetime
from rich.progress import track
from rich.console import Console

console = Console()

@dataclass
class Item:
    item: list[int] = field(default_factory=list)

    def set_item(self, item: list):
        self.item = item

        
@dataclass
class Items:
    items: list[Item] = field(default_factory=list)

menu_principal ={1: ['Clientes'],
                 2: ['Produtos'],
                 3: ['Ver premios'],
                 4: ['Sair'],
                }

def print_menu(menu):
    menu_table = table.Table( show_header=True, header_style="bold magenta",
                                 title="Menu", expand=True, highlight=True
                                )
    menu_table.add_column("ID", justify="center")
    menu_table.add_column("Opções", justify="left")
    for key, value in menu.items():
        menu_table.add_row(str(key), value[0])
    console.print(menu_table)

def main():
    items = Items()
    item = Item()
    item.set_item({"item_id": 101, "name": "butter"},)
    items.items.append(item)
    for v in items.items:
        print(v[item['item_id']])
        
    
    print()

if __name__ == '__main__':
	main()
        