def valid_password(password):
    
    if len(password) < 8:
        # print(password, "< 8")
        return False 
    if not any(char.islower() for char in password):
    #    print(password, "islower")
        return False
    if not any(char.isupper() for char in password):
    #    print(password, "isupper")
        return False
    if not any(char.isdigit() for char in password):
    #    print(password, "isdigit")
        return False
    
    return True

def import_and_create_bank(filename):
    bank = {}

    # your code here
    f =open(filename,'r')
    lines = f.readlines()
    
    for line in lines:
        lst = line.strip().split(':')
        
        if(len(lst)<=1):
            continue
        key = lst[0].strip()
        value = lst[1].strip()
        
        try:
            value = float(value)
            bank[key] = bank.get(key,0) + value
        except:
            continue

    return bank
        

def import_and_create_accounts(filename):
    user_accounts = {}
    user_login = {}

    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            lst = line.strip().split('-')

            
            if len(lst) <= 1:
                continue
            key = lst[0].strip()
            value = lst[1].strip()

            if (valid_password(value) and key not in user_accounts):
                user_accounts[key] = value
                user_login[key] = False
            else:
                continue

    return user_accounts, user_login

def signup(user_accounts, log_in, username, password):
        
    if username in user_accounts:
        print('Signup Failed User Already exists!')
        return False
    if not valid_password(password):
        print("Signup Failed Not a Valid PassWord")
        return False
    if username == password:
        return False
    
    user_accounts[username] = password
    log_in[username] = False
    print('User Succussfully created!')
    return True

def login(user_accounts, log_in, username, password):
    
    if(username in user_accounts) and (password == user_accounts.get(username)):
        log_in.update({username: True})
        print("User LoggedIn!")
        return True
    print("Login Failed Invalid UserName or Password!")
    return False

def update(bank, log_in, username, amount):
    if (log_in.get(username, False)):
        balance = bank.get(username, 0)
        new_balance = balance + amount
        
        if (new_balance >= 0):
            bank.update({username: new_balance})
            return True
        
    return False

def transfer(bank, log_in, userA, userB, amount):
    if(userB not in log_in): 
        print("Transfer Failed User not Logged in!")
        return False
    if(amount <=0): 
        print("Transfer Failed Amout Should more than 0")
        False
    if update(bank, log_in, userA, -amount):
        balance = bank.get(userB,0) + amount
        bank.update({userB : balance})
        print("Transaction Sucussful!")
        return True
    return False
    
def change_password(user_accounts, log_in, username, old_password, new_password):
    
    if(username not in user_accounts): 
        print('Change password failed User Not Found')
        return False
    
    if not(log_in.get(username)): 
        print("Change password failed User is not Logged in!")
        return False
    
    if not (user_accounts.get(username) == old_password): 
        print("Change password failed Your Old Password is same as your User name!")
        return False
    
    if(old_password == new_password):
        print("Change password failed Your Old passowrd and new password is the same!") 
        return False
    
    if(valid_password(new_password)):
        print("Change password failed Password Successfully Changed")
        user_accounts.update({username: new_password})
        
    else:
        print("Change password failed !")
        return False
        
    return True

def delete_account(user_accounts, log_in, bank, username, password):
    if (username not in user_accounts): 
        print("Delete account Failed UserName not Found!")
        return False
    if (log_in.get(username) and user_accounts.get(username) == password ):
        del user_accounts[username]
        del log_in[username]
        del bank[username]
        print("User Successfully Deleted")
        return True
    return False
        
    
    

def main():
    '''
    The main function is a skeleton for you to test if your overall programming is working.
    Note we will not test your main function. It is only for you to run and interact with your program.
    '''

    bank = import_and_create_bank(r"files/bank.txt")
    user_accounts, log_in = import_and_create_accounts(r"files/user.txt")

    while True:
        # for debugging
        # print('bank:', bank)
        # print('user_accounts:', user_accounts)
        # print('log_in:', log_in)
        # print('')
        #

        option = input("What do you want to do?  Please enter a numerical option below.\n"
        "1. login\n"
        "2. signup\n"
        "3. change password\n"
        "4. delete account\n"
        "5. update amount\n"
        "6. make a transfer\n"
        "7. exit\n")
        if option == "1":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to login
            login(user_accounts, log_in, username, password);
        elif option == "2":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to signup
            signup(user_accounts, log_in, username, password)
        elif option == "3":
            username = input("Please input the username\n")
            old_password = input("Please input the old password\n")
            new_password = input("Please input the new password\n")

            # add code to change password
            change_password(user_accounts, log_in, username, old_password, new_password)
        elif option == "4":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to delete account
            delete_account(user_accounts, log_in, bank, username, password)
        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to update amount
                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to transfer amount
                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "7":
            break;
        else:
            print("The option is not valid. Please re-enter the option.\n")
    
    
if __name__ == '__main__':
    main()