class EnergyNode:
    def __init__(self, id, production, consumption):
        self.id = id
        self.production = production
        self.consumption = consumption
        self.excess = production - consumption
        self.deficit = max(0, consumption - production)

def match_energy_trades(nodes):
    """
    Simple model for matching energy producers and consumers in a P2P network.
    
    :param nodes: List of EnergyNode objects
    :return: List of trades (tuples of seller, buyer, amount)
    """
    producers = sorted([n for n in nodes if n.excess > 0], key=lambda x: x.excess, reverse=True)
    consumers = sorted([n for n in nodes if n.deficit > 0], key=lambda x: x.deficit, reverse=True)
    
    trades = []
    for producer in producers:
        for consumer in consumers:
            if producer.excess > 0 and consumer.deficit > 0:
                trade_amount = min(producer.excess, consumer.deficit)
                trades.append((producer.id, consumer.id, trade_amount))
                producer.excess -= trade_amount
                consumer.deficit -= trade_amount
    
    return trades

# Example usage
nodes = [
    EnergyNode('A', 100, 80),
    EnergyNode('B', 50, 70),
    EnergyNode('C', 120, 90),
    EnergyNode('D', 30, 60)
]

trades = match_energy_trades(nodes)
for seller, buyer, amount in trades:
    print(f"Node {seller} sells {amount} KWH to Node {buyer}")
