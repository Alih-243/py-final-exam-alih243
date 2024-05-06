from bank import Bank
from users import Account_holder

def admin():
    while True:
        print('1. Create a new user account')
        print('2. Delete an existing account')
        print('3. View all user accounts')
        print('4. Check Bank vault balance')
        print('5. View total loan given')
        print('6. Switch Bank Bankrupt state')
        print('7. Exit from admin panel')
        choice = input('Enter choice: ')
        if choice == '1':
            name = input('Enter user\'s name: ')
            email = input('Enter user\'s email: ')
            address = input('Enter user\'s address: ')
            uname = input(f'Enter a username for {name}: ')
            key = input('Enter password: ')
            type = input('Account type: ')
            id = sampleBank.add_user(Account_holder(name, email, address, uname, key, type))
            print(f'Account for {name} created with id: {id.id}\n')
        elif choice == '2':
            id = input('Enter account id to delete: ')
            deleted = sampleBank.delete_user(id)
            if not deleted:
                print('User account not found\n')
            else:
                print(f'Deleted user account: {id}')
        elif choice == '3':
            result = sampleBank.show_all_accounts()
            if result == '':
                print('Bank currently has no user accounts\n')
            else:
                print(result)
        elif choice == '4':
            print(sampleBank.vault)
        elif choice == '5':
            print(sampleBank.loan_given)
        elif choice == '6':
            sampleBank.mayday()
        elif choice == '7':
            break
        else:
            print('Invalid input\n')

def user(user):
    while True:
        print('1. Deposit money')
        print('2. Withdraw money')
        print('3. Check account balance')
        print('4. Transfer money to another account')
        print('5. View transaction history')
        print('6. Request Loan')
        print('7. Exit from user panel')
        choice = input('Enter choice: ')
        if choice == '1':
            amount = int(input('Enter amount to deposit: '))
            sampleBank.add_money(user.id, amount, False)
            print('Success!\n')
        elif choice == '2':
            amount = int(input('Enter amount to withdraw: '))
            check = sampleBank.withdraw_money(amount, user.id)
            if check:
                print('Success\n')
        elif choice == '3':
            print('Balance:', sampleBank.check_balance(user.id), '\n')
        elif choice == '4':
            id = input('Enter reciever account id: ')
            amount = int(input('Enter transfer amount: '))
            found = sampleBank.transfer(user.id, id, amount)
            if found == True:
                print('Success\n')
            elif found == False:
                print('Account does not exist')
            else:
                print(found)
        elif choice == '5':
            result = sampleBank.history(user.id)
            if result == '':
                print('No transaction records\n')
            else:
                print(result)
        elif choice == '6':
            amount = int(input('Enter loan amount: '))
            sampleBank.get_loan(user.id, amount)
        elif choice == '7':
            break
        else:
            print('Invalid input\n')

sampleBank = Bank('Bank')

while True: # run initial interface
    print('1. User panel')
    print('2. Admin panel')
    print('3. Exit')
    choice = input('Enter choice: ')
    if choice == '1': # run user log in interface
        while True:
            print('1. Create account')
            print('2. Log in')
            print('3. Back to home')
            choice = input('Enter choice: ')
            if choice == '1':
                name = input('Enter your name: ')
                email = input('Enter your email: ')
                address = input('Enter your address: ')
                uname = input(f'Enter a username for {name}: ')
                key = input('Enter password: ')
                type = input('Account type: ')
                id = sampleBank.add_user(Account_holder(name, email, address, uname, key, type))
                print(f'Account for {name} created with id: {id.id}\n')
            elif choice == '2':
                if sampleBank.login_able():
                    uname = input(f'Enter username: ')
                    key = input('Enter password: ')
                    valid_user = sampleBank.find(uname, key)
                    if valid_user == False:
                        print('Invalid username or password\n')
                    else:
                        print(f'Welcome {valid_user.name}!\n')
                        user(valid_user)
                else:
                    print('Please sign up first\n')    
            elif choice == '3':
                break
            else:
                print('Invalid input\n')
    elif choice == '2':
        
        foo = input('Admin username: ')
        bar = int(input('Admin password: '))
        valid = sampleBank.is_admin(foo, bar)
        if valid:
            admin()
        else:
            print('Admin credentials don\'t match\n')
    elif choice == '3':
        break
    else:
        print('Invalid input\n')
            
