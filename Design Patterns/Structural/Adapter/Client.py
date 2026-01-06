from PaymentProcessor import InHousePaymentProcessor
from CheckoutService import CheckoutService
from LegacyGatewayAdapter import LegacyGatewayAdapter
from LegacyGateway import LegacyGateway
class ECommerceApp:
    @staticmethod
    def main():
        processor = InHousePaymentProcessor()
        checkout_service = CheckoutService(processor)
        checkout_service.checkout(100.00, "USD")

        legacy_processor = LegacyGateway()
        adapter = LegacyGatewayAdapter(legacy_processor)
        checkout_service_legacy = CheckoutService(adapter)
        checkout_service_legacy.checkout(120.00, "USD")

if __name__ == "__main__":
    ECommerceApp.main()
