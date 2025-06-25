import random
class Customer:
    def __init__(self, name, country, is_active, total_spent):
        self.name = name
        self.country = country
        self.is_active = is_active
        self.total_spent = total_spent

    def __repr__(self):
        return f"{self.name} - {self.country} - Active: {self.is_active} - Spent: ${self.total_spent:.2f}"


class CustomerQuery:
    def __init__(self, customers):
        self.customers = customers
        self.queryset = customers

    def active(self):
        self.queryset = [c for c in self.queryset if c.is_active]
        return self

    def from_country(self, country):
        self.queryset = [c for c in self.queryset if c.country == country]
        return self

    def with_min_spent(self, amount):
        self.queryset = [c for c in self.queryset if c.total_spent >= amount]
        return self

    def get(self):
        return self.queryset


names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hank", "Ivy", "Jack",
         "Karen", "Leo", "Mona", "Nina", "Oscar", "Pam", "Quinn", "Rick", "Sara", "Tom",
         "Uma", "Vince", "Wendy", "Xander", "Yara", "Zack", "Amy", "Ben", "Clara", "Dan"]

countries = ["USA", "Canada", "UK", "Germany", "France"]
customers = []

for name in names:
    country = random.choice(countries)
    is_active = random.choice([True, False])
    total_spent = round(random.uniform(100, 5000), 2)
    customers.append(Customer(name, country, is_active, total_spent))


query = CustomerQuery(customers)
filtered_customers = query.active().from_country("USA").with_min_spent(1000).get()

# 5. Imprimir resultados
print("Clientes filtrados:")
for customer in filtered_customers:
    print(customer)
