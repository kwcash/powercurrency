import datetime
import uuid

class Transaction:
    def __init__(self, sender, receiver, amount, transaction_type):
        self.id = str(uuid.uuid4())
        self.timestamp = datetime.datetime.now()
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.type = transaction_type  # 'send', 'receive', 'produce', 'consume'

class PowerCurrencyWallet:
    def __init__(self, address):
        self.address = address
        self.balance = 0
        self.transactions = []
        self.energy_production = 0
        self.energy_consumption = 0

    def check_balance(self):
        return self.balance

    def send(self, receiver, amount):
        if self.balance >= amount:
            self.balance -= amount
            transaction = Transaction(self.address, receiver, amount, 'send')
            self.transactions.append(transaction)
            return True
        return False

    def receive(self, sender, amount):
        self.balance += amount
        transaction = Transaction(sender, self.address, amount, 'receive')
        self.transactions.append(transaction)

    def produce_energy(self, amount):
        self.balance += amount
        self.energy_production += amount
        transaction = Transaction(self.address, self.address, amount, 'produce')
        self.transactions.append(transaction)

    def consume_energy(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.energy_consumption += amount
            transaction = Transaction(self.address, self.address, amount, 'consume')
            self.transactions.append(transaction)
            return True
        return False

    def get_transaction_history(self):
        return self.transactions

    def get_energy_stats(self):
        return {
            'production': self.energy_production,
            'consumption': self.energy_consumption
        }

def print_menu():
    print("\nPower Currency Wallet")
    print("1. Check Balance")
    print("2. Send Power Currency")
    print("3. Produce Energy")
    print("4. Consume Energy")
    print("5. View Transaction History")
    print("6. View Energy Stats")
    print("7. Exit")

def main():
    wallet = PowerCurrencyWallet("0x123456789")
    
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Current Balance: {wallet.check_balance()} PC")

        elif choice == '2':
            receiver = input("Enter receiver's address: ")
            amount = float(input("Enter amount to send: "))
            if wallet.send(receiver, amount):
                print("Transaction successful")
            else:
                print("Insufficient balance")

        elif choice == '3':
            amount = float(input("Enter amount of energy produced: "))
            wallet.produce_energy(amount)
            print(f"Added {amount} PC to your wallet")

        elif choice == '4':
            amount = float(input("Enter amount of energy to consume: "))
            if wallet.consume_energy(amount):
                print(f"Consumed {amount} PC from your wallet")
            else:
                print("Insufficient balance")

        elif choice == '5':
            history = wallet.get_transaction_history()
            for tx in history:
                print(f"{tx.timestamp} - {tx.type}: {tx.amount} PC")

        elif choice == '6':
            stats = wallet.get_energy_stats()
            print(f"Total Energy Produced: {stats['production']} PC")
            print(f"Total Energy Consumed: {stats['consumption']} PC")

        elif choice == '7':
            print("Thank you for using Power Currency Wallet!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
