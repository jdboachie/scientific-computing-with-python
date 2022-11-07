from math import floor



class Category:


    def __init__(self, category : str) -> None:
        """Initializes a category object

        Args:
            category (str): The category of the budget (eg. Food, )
        """

        self.category = category
        self.ledger = list()


    def deposit(self, amount : float, description = "") -> None:
        """Adds a deposit entry into the ledger

        Args:
            amount (int): The amount of money to be deposited
            description (str, optional): A short description of the transaction. Defaults to "".
        """
        round(amount, 2)
        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount : float, description = "") -> bool:
        """Adds a withdrawal entry into the ledger if eligible

        Args:
            amount (float): The amount to be withdrawn
            description (str, optional): A short description of the transaction. Defaults to "".

        Returns:
            bool: Returns True if the transaction is successful and False if not.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": amount * -1, "description": description})
            return True
        return False


    def get_balance(self) -> float:
        """Calculates the account balance from the ledger

        Returns:
            int: The account balance
        """

        balance = float()
        for entry in self.ledger:
            balance += entry["amount"]
        return balance


    def transfer(self, amount : float, category) -> bool:
        """Transfers funds from one budget category to another

        Args:
            amount (int): The amount to be transferred
            category (Category object): The budget category to transfer the amount to

        Returns:
            bool: Returns True if the transfer is successful else False
        """

        if self.check_funds(amount):
            self.withdraw(amount, description=f"Transfer to {category.category}")
            category.deposit(amount, description = f"Transfer from {self.category}")
            return True
        else:
            return False


    def check_funds(self, amount: float) -> bool:
        """Checks if a given amount is available in the account

        Args:
            amount (int): Given amount to check

        Returns:
            bool: Returns True if the amount is available else False
        """

        return self.get_balance() >= amount


    def __repr__(self) -> str:
        """__repr__

        Returns:
            str: A string representation of the Category object
        """

        rep = ""
        stars = ((30 - len(self.category)) // 2)
        rep = '*' * stars + self.category + '*' * stars + "\n"
        total = self.get_balance()
        amounts = [" " * (7 - len("%.2f" % round(x["amount"]))) + "%.2f" % round(x["amount"], 2) for x in self.ledger]
        descriptions = [x["description"] + " " * (23 - len(x["description"])) for x in self.ledger]
        
        # Cutting up to 23 characters
        descriptions = [x[:23] for x in descriptions]
        for i in range(len(self.ledger)):
            rep += descriptions[i] + amounts[i] + "\n"
        rep += f"Total: {total}"
        return rep



def create_spend_chart(categories : list) -> str:
    """Creates an expenditure bar chart

    Args:
        categories (list): A list of budget categories

    Returns:
        str: The expenditure chart based on the categories
    """

    # Getting category names
    names = [category.category for category in categories]
    max_length = max([len(x) for x in names])
    decorated_names = [name + " " * (max_length - len(name)) for name in names]

    # Getting withdrawals
    withdrawals = dict()
    for category in categories:
        withdrawals[category.category] = [entry["amount"] for entry in category.ledger if entry["amount"] < 0]
    
    # Calculating percentage by category
    total = sum(withdrawals[x][0] for x in names)
    percentages = [floor(((sum(withdrawals[name]) / total) * 100) / 10) for name in names]

    for i in range(len(percentages)):
        percentages[i] += 1

    bars = [" "* (11 - percentages[i]) + "o" * percentages[i] for i in range(len(percentages))]

    level_10 = "  ".join([bar[0] for bar in bars])
    level_9 = "  ".join([bar[1] for bar in bars])
    level_8 = "  ".join([bar[2] for bar in bars])
    level_7 = "  ".join([bar[3] for bar in bars])
    level_6 = "  ".join([bar[4] for bar in bars])
    level_5 = "  ".join([bar[5] for bar in bars])
    level_4 = "  ".join([bar[6] for bar in bars])
    level_3 = "  ".join([bar[7] for bar in bars])
    level_2 = "  ".join([bar[8] for bar in bars])
    level_1 = "  ".join([bar[9] for bar in bars])
    level_0 = "  ".join([bar[10] for bar in bars])


    name_levels = {}
    for i in range(max_length):
        name_levels[i] = [name[i] for name in decorated_names]

    name_strings = ""
    for x in name_levels:
        name_strings += "     " + "  ".join(name_levels[x]) + "  \n"
    name_strings = name_strings[:len(name_strings) - 1]

    bar_graph = f"""Percentage spent by category
100| {level_10}  
 90| {level_9}  
 80| {level_8}  
 70| {level_7}  
 60| {level_6}  
 50| {level_5}  
 40| {level_4}  
 30| {level_3}  
 20| {level_2}  
 10| {level_1}  
  0| {level_0}  
    {"---" * (len(names))}-
{name_strings}"""
    return bar_graph