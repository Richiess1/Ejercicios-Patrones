class Logger:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")


class emailService:
    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def enviar(self, destinatario: str, mensaje: str) -> None:
        self.logger.log(f"[EMAIL] Enviando email: {mensaje} a su cuenta")


class CuentaBancaria:
    def __init__(self, email_service: emailService) -> None:
        self.email_service = email_service

    def transferir(self, cantidad: float, usuario: str) -> None:
        mensaje = f"Se transfirieron ${cantidad}"
        self.email_service.logger.log(mensaje)
        self.email_service.enviar(usuario, mensaje)


# Prueba
logger = Logger()
email_service = emailService(logger)
cuenta = CuentaBancaria(email_service)

cuenta.transferir(100, "richie@esen.edu.sv")
