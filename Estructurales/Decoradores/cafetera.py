# 1. Clase base
class Bebida:
    def calcular_precio(self):
        return 1.00  # Café base cuesta $1.00


# 2. Clase base decoradora
class DecoradorBebida(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida

    def calcular_precio(self):
        return self.bebida.calcular_precio()


# 3. Decoradores específicos

class LecheDescremada(DecoradorBebida):
    def calcular_precio(self):
        return super().calcular_precio() + 0.50

class LecheSoya(DecoradorBebida):
    def calcular_precio(self):
        return super().calcular_precio() + 0.75

class LecheCoco(DecoradorBebida):
    def calcular_precio(self):
        return super().calcular_precio() + 1.00

class Canela(DecoradorBebida):
    def calcular_precio(self):
        return super().calcular_precio() + 0.25

class CremaBatida(DecoradorBebida):
    def calcular_precio(self):
        return super().calcular_precio() + 1.50

class Saborizante(DecoradorBebida):
    def calcular_precio(self):
        return super().calcular_precio() + 1.25

class BebidaMediana(DecoradorBebida):
    def calcular_precio(self):
        return super().calcular_precio() + 1.00

class BebidaGrande(DecoradorBebida):
    def calcular_precio(self):
        return super().calcular_precio() + 2.00


# 4. Crear bebida con café + leche descremada + canela + crema batida + 2x saborizante + bebida grande
bebida = Bebida()
bebida = LecheDescremada(bebida)
bebida = Canela(bebida)
bebida = CremaBatida(bebida)
bebida = Saborizante(bebida)
bebida = Saborizante(bebida)  # doble saborizante
bebida = BebidaGrande(bebida)

# 5. Mostrar el precio total
print(f"Precio total: ${bebida.calcular_precio():.2f}")
