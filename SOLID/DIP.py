# violates Dependency Inversion principle
class GmailClient:
    def send_email(self, recipient, subject, body):
        print("Sent gmail")

class EmailService:
    def __init__(self):
        self.gmail_client = GmailClient()

    def send_email(self, recipient, subject, body):
        self.gmail_client.send_email(recipient, subject, body)

# satisfies DIP
class EmailClient:
    def send_email(self, recipient, subject, body):
        pass
class GmailClient(EmailClient):
    def send_email(self, recipient, subject, body):
        print("Sent gmail")

class OutlookClient(EmailClient):
    def send_email(self, recipient, subject, body):
        print("Sent outlook email")

class EmailService:
    def __init__(self, email_client):
        self.email_client = email_client

    def send_email(self, recipient, subject, body):
        self.email_client.send_email(recipient, subject, body)

gmail_client = GmailClient()
email_service = EmailService(gmail_client)
email_service.send_email("podduturisanjana@gmail.com","ABC", 'XYZ')