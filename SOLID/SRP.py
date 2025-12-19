# violates SRP
class UserManager:
    def authenticate(self, username, password):
        print("User authenticated")

    def update_profile(self, user_id, profile_data):
        print("Updated user profile")

    def email_notify(self, email_address, message):
        print("Sent email notification")


# satisfies SRP
class UserAuthentication:
    def authenticate(self, username, password):
        print("User authenticated")


class UserProfile:
    def update_profile(self, user_id, profile_data):
        print("Updated user profile")


class EmailNotification:
    def email_notify(self, email_address, message):
        print("Sent email notification")
