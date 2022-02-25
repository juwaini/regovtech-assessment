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
        if self.balance >= amount:
            self.balance = self.balance - amount
            return True
        else:
            return False

    def __str__(self):
        return f"{self.id}: {self.name}'s account. Balance: {self.balance}"


if __name__ == "__main__":
    # Create Accounts list to store Account instances
    accounts = list()

    # Create 3 unique instances and store (append) in Accounts list
    a = Account('Abu', 10)
    accounts.append(a)

    b = Account('Baba', 50)
    accounts.append(b)

    c = Account('Chong', 100)
    accounts.append(c)

    print(accounts)

    # Tech debt: need to find a better way to refer to account
    # Any mutation to list will change account's reference ID
