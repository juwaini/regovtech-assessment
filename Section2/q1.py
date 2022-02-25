import uuid


class Account:
    def __init__(self, name, balance):
        self.id = uuid.uuid4()  # Using default Python UUID as ID
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f'Account {self.id} current balance is {self.balance}'

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            return 'Insufficient balance.'

    def __str__(self):
        return f"{self.id}: {self.name}'s account. Balance: {self.balance}"


if __name__ == "__main__":
    # Create Accounts list to store Account instances
    Accounts = dict()

    # Create 3 unique instances and store in Accounts dictionary with str-ed ID as key
    a = Account('Abu', 10)
    Accounts[a.id.hex] = a

    b = Account('Baba', 50)
    Accounts[b.id.hex] = b

    c = Account('Chong', 100)
    Accounts[c.id.hex] = c
