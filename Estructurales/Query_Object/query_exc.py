class Customer:
    def __init__(self, name, country, is_active, total_spent):
        self.name = name
        self.country = country
        self.is_active = is_active
        self.total_spent = total_spent

    def __repr__(self):
        return f"{self.name} - {self.country} - ${self.total_spent:.2f}"


class CustomerQuery:
    def __init__(self, customers):
        self.customers = customers
        self.queryset = customers.copy()

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


customers = [
    Customer("John Doe", "USA", True, 1500.00),
    Customer("Jane Smith", "Canada", True, 900.00),
    Customer("Alice Brown", "USA", False, 2000.00),
    Customer("Bob White", "Germany", True, 1100.00),
    Customer("Carlos Diaz", "Mexico", True, 300.00),
    Customer("Eva Müller", "Germany", False, 5000.00),
    Customer("Tom Lee", "USA", True, 950.00),
    Customer("Maria Garcia", "USA", True, 999.99),
    Customer("Liam Johnson", "UK", True, 2000.00),
    Customer("Olivia Wilson", "France", False, 3000.00),
    Customer("Noah Martinez", "USA", True, 500.00),
    Customer("Emma Davis", "Canada", True, 800.00),
    Customer("James Clark", "UK", False, 700.00),
    Customer("Sophia Rodriguez", "Mexico", True, 400.00),
    Customer("Benjamin Hall", "Germany", True, 1200.00),
    Customer("Mia Lewis", "USA", False, 1000.00),
    Customer("Lucas Allen", "France", True, 1700.00),
    Customer("Charlotte Young", "UK", False, 200.00),
    Customer("Henry Hernandez", "USA", True, 999.99),
    Customer("Amelia King", "Canada", True, 1150.00),
    Customer("Sebastian Wright", "USA", True, 300.00),
    Customer("Isabella Lopez", "Mexico", True, 850.00),
    Customer("Elijah Scott", "Germany", False, 600.00),
    Customer("Emily Green", "USA", False, 700.00),
    Customer("Aiden Baker", "UK", True, 250.00),
    Customer("Harper Adams", "France", True, 950.00),
    Customer("Logan Nelson", "USA", True, 100.00),
    Customer("Evelyn Hill", "Canada", False, 750.00),
    Customer("Daniel Rivera", "Mexico", True, 650.00),
    Customer("Aria Campbell", "Germany", True, 1250.00),
]

resultados = CustomerQuery(customers).active().from_country("USA").with_min_spent(1000).get()

for c in resultados:
    print(c)
