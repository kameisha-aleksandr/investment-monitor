class PriceAlert:

    def __init__(self, symbol, condition, value):
        self.symbol = symbol
        self.condition = condition
        self.value = value
        self.triggered = False

    def check(self, price):
        if self.condition == "below":
            return price < self.value

        if self.condition == "above":
            return price > self.value

        raise ValueError(f"Unknown condition: {self.condition}")

    def update(self, price):
        is_triggered = self.check(price)

        state_changed = is_triggered != self.triggered

        self.triggered = is_triggered

        return is_triggered, state_changed