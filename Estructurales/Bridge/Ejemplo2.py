# Implementor
class NotificationSender:
    def send(self, message):
        pass

# Concrete Implementors
class EmailSender(NotificationSender):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSSender(NotificationSender):
    def send(self, message):
        print(f"Sending SMS: {message}")

# Abstraction
class Notification:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)

# Refined Abstraction
class AlertNotification(Notification):
    def notify(self, message):
        print("ALERT:", end=" ")
        super().notify(message)

# Uso
email = EmailSender()
alert = AlertNotification(email)
alert.notify("System overload")

sms = SMSSender()
alert_sms = AlertNotification(sms)
alert_sms.notify("Backup completed")