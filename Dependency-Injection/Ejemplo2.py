class EmailService:
    def enviar(self, destinatario, mensaje):
        print(f"Enviando email a {destinatario}: {mensaje}")

class Notificador:
    def __init__(self, servicio_mensaje):
        self.servicio = servicio_mensaje

    def notificar_usuario(self, usuario, mensaje):
        self.servicio.enviar(usuario, mensaje)

# Uso
email_service = EmailService()
notificador = Notificador(email_service)
notificador.notificar_usuario("juan@example.com", "Bienvenido")