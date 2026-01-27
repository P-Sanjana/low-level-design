from ShippingStrategy import FlatRateShipping, WeightBasedShipping
from ShippingCostService import ShippingCostService
class Order:
    def __init__(self, weight):
        self.weight = weight
    def get_total_weight(self):
        return self.weight

class Client:
    @staticmethod
    def main():
        flat_rate = FlatRateShipping(5)
        weight_rate = WeightBasedShipping(10)

        shipping_cost_service = ShippingCostService(flat_rate)
        order = Order(4)
        print(f'flat rate: {shipping_cost_service.calculate_shipping_cost(order)}')

        shipping_cost_service.set_strategy(weight_rate)
        print(f'Weight rate: {shipping_cost_service.calculate_shipping_cost(order)}')

if __name__ == '__main__':
    Client.main()
