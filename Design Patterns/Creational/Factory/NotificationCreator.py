from abc import ABC, abstractmethod
import Notification
class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self):
        pass

    def send(self, message):
        notification = self.create_notification()
        notification.send(message)

class EmailNotificationCreator(NotificationCreator):
    def create_notification(self):
        return Notification.EmailNotification()

class SMSNotificationCreator(NotificationCreator):
    def create_notification(self):
        return Notification.SMSNotification()

class PushNotificationCreator(NotificationCreator):
    def create_notification(self):
        return Notification.PushNotification()

email_notifier = EmailNotificationCreator()
email_notifier.send("email message")

sms_notifier = SMSNotificationCreator()
sms_notifier.send("SMS message")
