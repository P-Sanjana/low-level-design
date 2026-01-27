from abc import ABC, abstractmethod
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, order):
        pass

class FlatRateShipping(ShippingStrategy):
    def __init__(self, rate):
        self.rate = rate

    def calculate_cost(self, order):
        return self.rate

class WeightBasedShipping(ShippingStrategy):
    def __init__(self, rate_per_lb):
        self.rate_per_lb = rate_per_lb

    def calculate_cost(self, order):
        return order.get_total_weight() * self.rate_per_lb

