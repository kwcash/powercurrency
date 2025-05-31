class PowerCurrencyContract:
    def __init__(self):
        self.balances = {}
        self.energy_production = {}
        self.energy_consumption = {}
        self.exchange_rate = 1  # 1 KWH = 1 Power Currency unit

    def mint(self, address, amount):
        """Mint new Power Currency based on energy production"""
        if address not in self.balances:
            self.balances[address] = 0
        self.balances[address] += amount
        if address not in self.energy_production:
            self.energy_production[address] = 0
        self.energy_production[address] += amount

    def transfer(self, from_address, to_address, amount):
        """Transfer Power Currency between addresses"""
        if from_address not in self.balances or self.balances[from_address] < amount:
            return False
        if to_address not in self.balances:
            self.balances[to_address] = 0
        self.balances[from_address] -= amount
        self.balances[to_address] += amount
        return True

    def consume_energy(self, address, amount):
        """Record energy consumption and deduct from balance"""
        if address not in self.balances or self.balances[address] < amount:
            return False
        self.balances[address] -= amount
        if address not in self.energy_consumption:
            self.energy_consumption[address] = 0
        self.energy_consumption[address] += amount
        return True

    def get_balance(self, address):
        """Get the balance of an address"""
        return self.balances.get(address, 0)

    def get_energy_production(self, address):
        """Get the total energy production of an address"""
        return self.energy_production.get(address, 0)

    def get_energy_consumption(self, address):
        """Get the total energy consumption of an address"""
        return self.energy_consumption.get(address, 0)

# Example usage
contract = PowerCurrencyContract()

# Simulate energy production
contract.mint("Alice", 100)  # Alice produces 100 KWH
contract.mint("Bob", 50)     # Bob produces 50 KWH

# Simulate energy transfer
contract.transfer("Alice", "Charlie", 30)  # Alice transfers 30 units to Charlie

# Simulate energy consumption
contract.consume_energy("Bob", 20)  # Bob consumes 20 KWH

# Check balances and energy stats
print("Alice's balance:", contract.get_balance("Alice"))
print("Bob's balance:", contract.get_balance("Bob"))
print("Charlie's balance:", contract.get_balance("Charlie"))
print("Alice's total energy production:", contract.get_energy_production("Alice"))
print("Bob's total energy consumption:", contract.get_energy_consumption("Bob"))
