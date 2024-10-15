import random
import time

class EnergyNode:
    def __init__(self, id, production_capacity, consumption_rate):
        self.id = id
        self.production_capacity = production_capacity
        self.consumption_rate = consumption_rate
        self.balance = 0
        self.energy_surplus = 0
        self.energy_deficit = 0

    def produce_energy(self):
        production = random.uniform(0.5 * self.production_capacity, self.production_capacity)
        consumption = random.uniform(0.5 * self.consumption_rate, self.consumption_rate)
        net_energy = production - consumption
        self.balance += net_energy
        if net_energy > 0:
            self.energy_surplus = net_energy
            self.energy_deficit = 0
        else:
            self.energy_surplus = 0
            self.energy_deficit = -net_energy
        return net_energy

class EnergyMarket:
    def __init__(self):
        self.nodes = []
        self.transactions = []

    def add_node(self, node):
        self.nodes.append(node)

    def execute_trades(self):
        sellers = sorted([n for n in self.nodes if n.energy_surplus > 0], 
                         key=lambda x: x.energy_surplus, reverse=True)
        buyers = sorted([n for n in self.nodes if n.energy_deficit > 0], 
                        key=lambda x: x.energy_deficit, reverse=True)
        
        for seller in sellers:
            for buyer in buyers:
                if seller.energy_surplus > 0 and buyer.energy_deficit > 0:
                    trade_amount = min(seller.energy_surplus, buyer.energy_deficit)
                    price = trade_amount * random.uniform(0.08, 0.12)  # Price per kWh
                    self.transactions.append({
                        'seller': seller.id,
                        'buyer': buyer.id,
                        'amount': trade_amount,
                        'price': price
                    })
                    seller.energy_surplus -= trade_amount
                    buyer.energy_deficit -= trade_amount
                    seller.balance += price
                    buyer.balance -= price

    def simulate_day(self):
        for _ in range(24):  # 24 hours in a day
            for node in self.nodes:
                node.produce_energy()
            self.execute_trades()

    def print_daily_report(self):
        print("\nDaily Report:")
        for node in self.nodes:
            print(f"Node {node.id}: Balance = {node.balance:.2f} kWh")
        print(f"Total Transactions: {len(self.transactions)}")
        total_energy_traded = sum(t['amount'] for t in self.transactions)
        print(f"Total Energy Traded: {total_energy_traded:.2f} kWh")

def run_simulation(days=7):
    market = EnergyMarket()
    
    # Create nodes with random production and consumption rates
    for i in range(10):
        production = random.uniform(10, 50)
        consumption = random.uniform(10, 50)
        market.add_node(EnergyNode(i, production, consumption))
    
    for day in range(days):
        print(f"\n--- Day {day + 1} ---")
        market.simulate_day()
        market.print_daily_report()

if __name__ == "__main__":
    run_simulation()
