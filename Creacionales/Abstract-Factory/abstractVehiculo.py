from abc import ABC, abstractmethod

# Interfaces Abstractas
class Vehiculo(ABC):
    @abstractmethod
    def render(self):
        pass

class Motor(ABC):
    @abstractmethod
    def render(self):
        pass

# Vehículos concretos
class Carro(Vehiculo):
    def render(self):
        print("Creando vehículo terrestre: Carro")

class Lancha(Vehiculo):
    def render(self):
        print("Creando vehículo acuático: Lancha")

# Motores concretos
class MotorDeCombustion(Motor):
    def render(self):
        print("Usando motor: Motor de combustión")

class MotorNautico(Motor):
    def render(self):
        print("Usando motor: Motor náutico")

# Fábrica abstracta
class FabricaVehiculos(ABC):
    @abstractmethod
    def crear_vehiculo(self) -> Vehiculo:
        pass

    @abstractmethod
    def crear_motor(self) -> Motor:
        pass

# Fábricas concretas
class FabricaTerrestre(FabricaVehiculos):
    def crear_vehiculo(self) -> Vehiculo:
        return Carro()

    def crear_motor(self) -> Motor:
        return MotorDeCombustion()

class FabricaAcuatica(FabricaVehiculos):
    def crear_vehiculo(self) -> Vehiculo:
        return Lancha()

    def crear_motor(self) -> Motor:
        return MotorNautico()

# Cliente
def cliente(fabrica: FabricaVehiculos):
    vehiculo = fabrica.crear_vehiculo()
    motor = fabrica.crear_motor()
    vehiculo.render()
    motor.render()

# Prueba
cliente(FabricaTerrestre())

cliente(FabricaAcuatica())
