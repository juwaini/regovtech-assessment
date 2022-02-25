from q1 import Account


class DevAccount(Account):
    def set_balance(self, amount):
        self.balance = amount
        return f"Done reset account balance. {self.id}: {self.name}'s account. Balance: {self.balance}"

    def get_balance(self):
        return f"{self.id}: {self.name}'s account. Balance: {self.balance}"

    def transfer_to_other_account(self, amount, accounts_list, account_id):
        # data structure 'accounts_list' is a list, let's check if id exists
        if account_id >= len(accounts) or account_id < 0:
            return f'Account ID {account_id} not exists.'
        else:
            account_to_transfer = accounts_list[account_id]
            if self.withdraw(amount):
                account_to_transfer.deposit(amount)
            else:
                return f'Insufficient balance.'


if __name__ == "__main__":
    # Create Accounts list to store Account instances
    accounts = list()

    # Create 3 unique instances and store (append) in Accounts list
    a = DevAccount('Abu', 10)
    accounts.append(a)

    b = DevAccount('Baba', 50)
    accounts.append(b)

    c = DevAccount('Chong', 100)
    accounts.append(c)

    # print(accounts)

    # Basic unit tests
    abu = accounts[0]
    baba = accounts[1]
    chong = accounts[2]
    # print(abu.transfer_to_other_account(20, accounts, 1))  # Should be failed, not enough balance.
    # abu.transfer_to_other_account(10, accounts, 1)  # Success
    # print(abu.balance)
    assert abu.balance == 0
    assert baba.balance == 60
