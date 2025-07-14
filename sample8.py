class Bank:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        
        self.accounts = []
        
    def addAccount(self, account):
        self.accounts.append(account)
    def removeAccount(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
    def getTotalBalance(self):
        return sum(account['balance'] for account in self.accounts)
    
if __name__ == "__main__":
    my_bank = Bank("My Bank", "123 Main St")

    account1 = {"account_number": "1", "account_name": "Account Name: Alice", "balance": 1000}
    account2 = {"account_number": "2", "account_name": "Account Name: Bob", "balance": 1500}
    my_bank.addAccount(account1)
    my_bank.addAccount(account2)
    
    # my_bank.removeAccount(account2)
    
    print("Total Balance:", my_bank.getTotalBalance())