class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


class ProductQuery:
    def __init__(self, products):
        self.products = products

    def with_min_price(self, min_price):
        self.products = [p for p in self.products if p.price >= min_price]
        return self

    def in_category(self, category):
        self.products = [p for p in self.products if p.category == category]
        return self

    def result(self):
        return self.products


# Sample usage
products = [
    Product("T-Shirt", 25, "Clothing"),
    Product("Laptop", 900, "Electronics"),
    Product("Shoes", 60, "Clothing")
]

query = ProductQuery(products)
filtered = query.in_category("Clothing").with_min_price(30).result()

for p in filtered:
    print(f"{p.name}: ${p.price}")