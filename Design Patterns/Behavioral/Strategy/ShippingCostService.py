class ShippingCostService:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate_shipping_cost(self, order):
        if self.strategy is None:
            raise ValueError("Strategy not defined")

        cost = self.strategy.calculate_cost(order)
        print(f'Cost: {cost}')
