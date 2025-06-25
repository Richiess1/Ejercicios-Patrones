import json
from abc import ABC, abstractmethod

class ProcesadorPago(ABC):
    @abstractmethod
    def procesar_pago(self, json_data):
        pass

class PagoModerno(ProcesadorPago):
    def procesar_pago(self, json_data):
        data = json.loads(json_data)
        print(f"[MODERNO] Procesando pago de {data['amount']} {data['currency']} para usuario {data['user_id']}")

class ServicioPagoLegacy:
    def pagar(self, datos_legacy):
        print(f"[LEGACY] Procesando pago para cliente {datos_legacy['cliente']} por {datos_legacy['monto_total']} {datos_legacy['moneda']}")

class PagoAdapter(ProcesadorPago):
    def __init__(self, servicio_legacy):
        self.servicio_legacy = servicio_legacy

    def procesar_pago(self, json_data):
        data = json.loads(json_data)
        print("[JSON moderno recibido]", data)

        datos_legacy = {
            "cliente": data["user_id"],
            "monto_total": data["amount"],
            "moneda": data["currency"]
        }
        print("[Adaptado a legacy]", datos_legacy)

        self.servicio_legacy.pagar(datos_legacy)

if __name__ == "__main__":
    json_input = json.dumps({
        "user_id": "u123",
        "amount": 250.0,
        "currency": "USD"
    })

    print("\n--- Uso de clase moderna ---")
    moderno = PagoModerno()
    moderno.procesar_pago(json_input)

    print("\n--- Uso de clase legacy con adaptador ---")
    legacy = ServicioPagoLegacy()
    adaptador = PagoAdapter(legacy)
    adaptador.procesar_pago(json_input)
