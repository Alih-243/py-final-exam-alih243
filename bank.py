class Bank:
    def __init__(self, name) -> None:
        self.name = name 
        self.__users = [] # list user object
        self.__admin = {'admin': 123}
        self.__vault = 314159265
        self.bankrupt = False
        self.loan_given = 0
    
    # bank functions

    def find(self, uname, key):
        for user in self.__users:
            if user.username == uname and user.key == key:
                return user
        return False
    
    def is_admin(self, username, key):
        if username in self.__admin.keys():
            if self.__admin[username] == key:
                return True
            else:
                return False
        return False
    
    def login_able(self):
        if len(self.__users):
            return True
        return False

    @property
    def vault(self):
        return self.__vault
    
    def add_to_vault(self, amount):
        self.__vault += amount

    def cut_from_vault(self, amount):
        self.__vault -= amount
    
    def mayday(self):
        if self.bankrupt == True:
            self.bankrupt = False
        else:
            self.bankrupt = True

    # admin related functions

    def add_user(self, user):
        user.id = f'{user.username}-{len(self.__users) + 1}'
        self.__users.append(user)
        return user

    def delete_user(self, id):
        deleted = False
        for i, user in enumerate(self.__users):
            if user.id == id:
                del self.__users[i]
                deleted = True
                break
        return deleted
    
    def show_all_accounts(self):
        result = ''
        for user in self.__users:
            result += f'ID: {user.id}\tBalance: {user.balance}\tType: {user.type}\n'
        return result

    # user related functions

    def add_money(self, id, amount, loan):
        message = 'Deposited amount'
        if loan:
            message = 'Loan requested amount'
        for user in self.__users:
            if user.id == id:
                user.balance = f'+{amount}'
                self.add_to_vault(amount)
                user.history.append(f'{len(user.history) + 1}. {message}: {amount}')
                break
    
    def withdraw_money(self, amount, id):
        withdrawn = False
        if self.bankrupt:
            print('Bank currently is bankrupt')
            return
        for user in self.__users:
            if user.id == id:
                if user.balance >= amount:
                    user.balance = f'-{amount}'
                    self.cut_from_vault(amount)
                    user.history.append(f'{len(user.history) + 1}. Money withdraw amount: {amount}')
                    withdrawn = True
                else:
                    print('Withdrawal amount exceeded\n')
                    user.history.append(f'{len(user.history) + 1}. Failed withdraw attempt amount: {amount}')
                break
        return withdrawn

    def history(self, id):
        for user in self.__users:
            if user.id == id:
                break
        result = ''
        for record in user.history:
            result += f'{record}\n'
        return result

    def check_balance(self, id):
        for user in self.__users:
            if user.id == id:
                return user.balance
    
    def get_loan(self, id, amount):
        if not self.bankrupt:
            for user in self.__users:
                if user.id == id:
                    break
            if user.loan_count:
                self.add_money(user.id, amount, True)
                user.loan_count -= 1
                self.loan_given += amount
                print('Loan money has been added to your account.\n')
            else:
                print('You have exhasted your loan requests.\n')

        else:
            print('Loan requests are off due to bankrupt.\n')
    
    def transfer(self, self_id, other_id, amount):
        found = False
        if self.bankrupt:
            return 'The Bank has gone bankrupt, transferring is off'
        message1 = f'Money transfered to {other_id}'
        message2 = f'Money recieved from {self_id}'
        for user1 in self.__users:
            if user1.id == self_id:
                break
        for user2 in self.__users:
            if user2.id == other_id:
                found = True
                break
        if found:
            user1.balance = f'-{amount}'
            user1.history.append(f'{len(user1.history) + 1}. {message1}: {amount}')
            user2.balance = f'+{amount}'
            user2.history.append(f'{len(user2.history) + 1}. {message2}: {amount}')
        return found
