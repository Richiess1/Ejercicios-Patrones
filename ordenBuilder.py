class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}" 


class Order:
    def __init__(self):
        self.user = None
        self.products = []
        self.address = None
        self.payment_method = None
        self.discount = False
        self.discount_amount = 0.0 
        self.calculadora = None

    def __str__(self):
        total = self.calculadora.calcular(self) if self.calculadora else 0.0
        return (
            f"--------------------------------------------------\n"
            f"Orden para {self.user}:\n"
            f"Productos: {', '.join(str(product) for product in self.products)}.\n"
            f"Dirección: {self.address}.\n"
            f"Metodo de pago: {self.payment_method}.\n"
            f"--------------------------------------------------\n"
            f"Resumen de la orden:\n"
            f"--------------------------------------------------\n"
            f"Descuento aplicado: {self.discount}.\n"
            f"Total de descuento: ${self.discount_amount:.2f}\n"
            f"Total de productos: ${sum(product.price for product in self.products):.2f}\n"
            f"Total a pagar menos decuento: ${total:.2f}\n"
            f"Gracias por su compra {self.user}!\n"
            f"--------------------------------------------------\n"
            f"Almacenes SIMAN - Tu mejor opción en tecnología y más!\n"

        )


class OrdenBuider:
    def __init__(self):
        self.order = Order()
        self.calculadora = CaluladorDeTotal()


    def set_user(self, user: str):
        self.order.user = user
        return self
    
    def add_product(self, product: Product):
        self.order.products.append(product)
        return self
    
    def set_address(self, address: str):    
        self.order.address = address
        return self
    
    def set_payment_method(self, payment_method: str):
        self.order.payment_method = payment_method
        return self
    

    def build(self):
        if not self.order.user or not self.order.products or not self.order.address or not self.order.payment_method:
            raise Exception("La orden debe tener un usuario, productos, dirección y método de pago.")
        
        self.order.calculadora = self.calculadora
        return self.order
    
class CaluladorDeTotal:
    def calcular(self, order: Order):
        total = sum(product.price for product in order.products)
        descuento = 0

        if total > 400:
            descuento = total * 0.20
            order.discount = True
        elif total > 300:
            descuento = total * 0.15
            order.discount = True
        elif total > 200:
            descuento = total * 0.10
            order.discount = True
        elif total > 100:
            descuento = total * 0.05
            order.discount = True
        else:
            order.discount = False

        order.discount_amount = descuento 
        return total - descuento

    

# Ejemplo 1
# creando productos
Laptop_HP = Product("Laptop", 999.99)
Celular_Samsung = Product("Celular", 499.99)
Mouse_Logitech = Product("Mouse", 49.99)
Cargador_Apple = Product("Cargador", 59.99)
cargador_Samsung = Product("Cargador Samsung", 29.99)

# creando orden
orden1 = OrdenBuider()\
    .set_user("Ricardo Cubias")\
    .add_product(Laptop_HP)\
    .add_product(Celular_Samsung)\
    .add_product(Mouse_Logitech)\
    .add_product(Cargador_Apple)\
    .set_address("Av. Los Bambues, Casa 5 - E")\
    .set_payment_method("Tarjeta de Crédito")\
    .build()


# Imprimiendo orden y total
print(orden1)

        
    








