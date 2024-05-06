class User:
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address

class Account_holder(User):
    def __init__(self, name, email, address, username, key, type) -> None:
        super().__init__(name, email, address)
        self.id = None
        self.__username = username
        self.__key = key
        self.__balance = 0
        self.type = type
        self.loan_count = 2
        self.history = []
    
    @property
    def username(self):
        return self.__username
    
    @property
    def key(self):
        return self.__key
    
    @property
    def balance(self):
        return self.__balance
    
    def add_to_balance(self, amount):
        self.__balance += amount

    def cut_from_balance(self, amount):
        self.__balance -= amount

    @balance.setter
    def balance(self, magic):
        sign = magic[0]
        amount = magic[1:]
        amount = int(amount)
        if sign == '+':
            self.add_to_balance(amount)
        else:
            self.cut_from_balance(amount)
