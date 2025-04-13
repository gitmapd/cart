import csv
def load_items_from_file(file_path, inventory):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            codigo = row['codigo']
            nome = row['nome']
            preco = float(row['preco'])
            inventory.add_item(codigo, nome, preco)