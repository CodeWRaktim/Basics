class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, customer_name, initial_balance):
        self.accounts[account_number] = {
            "customer_name": customer_name,
            "balance": initial_balance
        }

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            print("Deposit successful.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def get_balance(self, account_number):
        if account_number in self.accounts:  
            return self.accounts[account_number]["balance"]
        else:
            return "Account not found."

# Example usage
bank = Bank()
bank.create_account(12345, "John Doe", 1000)
bank.deposit(12345, 500)
bank.withdraw(12345, 200)
balance = bank.get_balance(12345)
print("Balance:", balance)