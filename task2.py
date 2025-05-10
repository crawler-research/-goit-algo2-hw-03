import csv
import timeit
from BTrees.OOBTree import OOBTree

def load_product_data(file_path):
    products = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            products.append((int(row[0]), row[1]))
    return products

def add_item_to_tree(tree, product):
    tree.insert(product[0], product[1])

def add_item_to_dict(dictionary, product):
    dictionary[product[0]] = product[1]

def range_query_tree(tree, start, end):
    return [item for key, item in tree.items() if start <= key <= end]

def range_query_dict(dictionary, start, end):
    return [item for key, item in dictionary.items() if start <= key <= end]

file_path = 'products.csv'
products = load_product_data(file_path)

tree = OOBTree()
dictionary = {}

for product in products:
    add_item_to_tree(tree, product)
    add_item_to_dict(dictionary, product)


tree_time = timeit.timeit(lambda: range_query_tree(tree, 10, 50), number=1000)
dict_time = timeit.timeit(lambda: range_query_dict(dictionary, 10, 50), number=1000)

print(f"Time taken for OOBTree range query: {tree_time:.6f} seconds")
print(f"Time taken for dictionary range query: {dict_time:.6f} seconds")