# Productos
class Boton:
    def render(self):
        pass

class Ventana:
    def render(self):
        pass

# Familia: Tema claro
class BotonClaro(Boton):
    def render(self):
        print("Botón con estilo claro")

class VentanaClara(Ventana):
    def render(self):
        print("Ventana con estilo claro")

# Familia: Tema oscuro
class BotonOscuro(Boton):
    def render(self):
        print("Botón con estilo oscuro")

class VentanaOscura(Ventana):
    def render(self):
        print("Ventana con estilo oscuro")

# Abstract Factory
class UIFactory:
    def crear_boton(self) -> Boton:
        pass
    def crear_ventana(self) -> Ventana:
        pass

# Concrete Factories
class TemaClaroFactory(UIFactory):
    def crear_boton(self):
        return BotonClaro()
    def crear_ventana(self):
        return VentanaClara()

class TemaOscuroFactory(UIFactory):
    def crear_boton(self):
        return BotonOscuro()
    def crear_ventana(self):
        return VentanaOscura()

# Cliente
def construir_interfaz(factory: UIFactory):
    boton = factory.crear_boton()
    ventana = factory.crear_ventana()
    boton.render()
    ventana.render()

# Uso
construir_interfaz(TemaClaroFactory())
construir_interfaz(TemaOscuroFactory())