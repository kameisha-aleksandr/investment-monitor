class PriceAlert:

    def __init__(self, symbol, condition, value):
        self.symbol = symbol
        self.condition = condition
        self.value = value

    def check(self, price):
        if self.condition == "below":
            return price < self.value

        if self.condition == "above":
            return price > self.value

        raise ValueError(f"Unknown condition: {self.condition}")