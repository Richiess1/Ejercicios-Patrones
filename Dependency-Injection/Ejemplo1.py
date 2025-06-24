class Motor:
    def encender(self):
        print("Motor encendido")

class Coche:
    def __init__(self, motor):
        self.motor = motor

    def arrancar(self):
        self.motor.encender()

# Inyección manual
mi_motor = Motor()
mi_coche = Coche(mi_motor)
mi_coche.arrancar()