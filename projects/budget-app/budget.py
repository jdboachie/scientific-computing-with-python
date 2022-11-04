class Category:


    def __init__(self, category : str) -> None:
        self.category = category
        self.ledger = list()


    def deposit(self, amount : int, description = ""):
        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount : float, description):
        if self.check_funds():
            self.ledger.append({"amount": amount * -1, "description": description})
            return True
        return False


    def get_balance(self) -> int:
        total = int()
        for entry in self.ledger:
            total += entry["amount"]
        return total


    def transfer(self, amount : int, category):
        if self.check_funds():
            self.withdraw(amount, description=f"Transfer to {category.category}")
            category.deposit(amount, description = f"Transfer from {self.category}")
            return True
        else:
            return False


    def check_funds(self, amount: int) -> bool:
        return self.get_balance() <= amount


    def __repr__(self) -> str:
        pass

def create_spend_chart(categories):
    pass
