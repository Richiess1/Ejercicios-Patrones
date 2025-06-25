class Product:
    def __init__(self, price):
        self.price = price

    def calculate_price(self):
        print(f"[Base] Initial price: ${self.price:.2f}")
        return self.price


class TaxDecorator:
    def __init__(self, component):
        self.component = component

    def calculate_price(self):
        base_price = self.component.calculate_price()
        tax = base_price * 0.15
        total = base_price + tax
        print(f"[Tax] Adding 15% tax: +${tax:.2f} → ${total:.2f}")
        return total


class DiscountDecorator:
    def __init__(self, component):
        self.component = component

    def calculate_price(self):
        base_price = self.component.calculate_price()
        discount = 10
        total = base_price - discount
        print(f"[Discount] Subtracting fixed discount: -${discount:.2f} → ${total:.2f}")
        return total
        
if __name__ == "__main__":
	product = Product(100)
	product_with_tax = TaxDecorator(product)
	final_product = DiscountDecorator(product_with_tax)
	
	final_price = final_product.calculate_price()
	print(f"\n[Result] Final price: ${final_price:.2f}")