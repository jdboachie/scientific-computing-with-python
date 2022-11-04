class Category:


    def __init__(self, category : str) -> None:
        """Initializes a category object

        Args:
            category (str): The category of the budget (eg. Food, )
        """

        self.category = category
        self.ledger = list()


    def deposit(self, amount : int, description = "") -> None:
        """Adds a deposit entry into the ledger

        Args:
            amount (int): The amount of money to be deposited
            description (str, optional): A short description of the transaction. Defaults to "".
        """

        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount : float, description = "") -> bool:
        """Adds a withdrawal entry into the ledger if eligible

        Args:
            amount (float): The amount to be withdrawn
            description (str, optional): A short description of the transaction. Defaults to "".

        Returns:
            bool: Returns True if the transaction is successful and False if not.
        """

        if self.check_funds():
            self.ledger.append({"amount": amount * -1, "description": description})
            return True
        return False


    def get_balance(self) -> int:
        """Calculates the account balance from the ledger

        Returns:
            int: The account balance
        """

        balance = int()
        for entry in self.ledger:
            balance += entry["amount"]
        return balance


    def transfer(self, amount : int, category) -> bool:
        """Transfers funds from one budget category to another

        Args:
            amount (int): The amount to be transferred
            category (Category object): The budget category to transfer the amount to

        Returns:
            bool: Returns True if the transfer is successful else False
        """

        if self.check_funds():
            self.withdraw(amount, description=f"Transfer to {category.category}")
            category.deposit(amount, description = f"Transfer from {self.category}")
            return True
        else:
            return False


    def check_funds(self, amount: int) -> bool:
        """Checks if a given amount is available in the account

        Args:
            amount (int): Given amount to check

        Returns:
            bool: Returns True if the amount is available else False
        """

        return self.get_balance() <= amount


    def __repr__(self) -> str:
        """__repr__

        Returns:
            str: A string representation of the Category object
        """

        pass



def create_spend_chart(categories : list) -> str:
    """Creates an expenditure chart

    Args:
        categories (list): A list of budget categories

    Returns:
        str: The expenditure chart based on the categories
    """

    
