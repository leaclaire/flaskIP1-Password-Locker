#!/usr/bin/env python3.8
# from credentials import Credentials
# from account import Account
# from generate import *

       #Account

def create_account(account_name, user_name, password):
    '''
    function to create a new account
    '''
    new_account = Account(account_name, user_name, password)
    return new_account


def save_accounts(account):
    '''
    function to save account
    '''
    account.save_accounts()


def check_account_exists(user_name, password):
    '''
    Function that check if a account exists with that password and a username and return a Boolean
    '''
    return Account.account_exists(user_name, password)

            #Credentials
def create_credentials(account, username, password):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(account, username, password)
    return new_credentials


def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def check_existing_credentials(username):
    '''
    function that checks if a credential exists with that username
    '''
    return Credentials.credentials_exist(username)    


def delete_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()


def find_credentials(username):
    '''
    Function that finds an account by username and returns the credentials
    '''
    return Credentials.find_by_username(username)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

            #Main

def main():
    print("Hello there, welcome to Password-lockcer, your passwords are safe with us, you can also create your own and store it here.")
    while True:
        print('\n')
        print('-'*10)
        print('Use these short codes carefully, to navigate : cu - Create a new account, lg - login to your account, ex -exit the password locker')
        print('-'*10)

        shortCode = input().lower()

        if shortCode == 'cu':
            print('Enter your username')
            username = input()

            passResponse = input(
                'Do you want a generated password? \n  Respond with \'y\' for yes or \'n\' for no: ').lower()

            if passResponse == 'y':
                createdPass = passwordGenerator(getPassLength())
                password = createdPass

                print(f'''
                Your generated password ({str(len(createdPass))}):
                is as shown below...

                {createdPass}
                ''')
            else:

                print("What's your password")
                password = input()
                print("Confirm password ....")
                confirm_password = input()

                while confirm_password != password:
                    print(" Oppss!!! Password did not match")
                    print("Enter the right password ....")
                    password = input()
                    print("Confirm your password ....")
                    confirm_password = input()

                else:
                    save_accounts(create_account(username,password,password))
                    print(
                        f'Congratulations 🎉, Succefully created a new a count for: {username} using this password: {password}')
                    print("Proceed to login")
                    print("username")
                    entered_username = input()
                    print("your password")
                    entered_password = input()

        elif shortCode == 'lg':
            print('Enter your username: ')
            defaultUserName = input()

            print('Enter password: ')
            defaultPassword = input()
            print('\n')
            print('Login success! \n')
            print('\n')

            while entered_username != username or entered_password != password:
                print("Invalid username or password")
                print('username')
                entered_username = input()
                print("Your password")
                entered_password = input()
            else:

                print(
                    f'Welcome back to password locker  {entered_username} 😍. Please choose an option to continue')

                while True:
                    print('\n ………')
                    print(
                        'Please use  these short codes to navigate through credentials : ac - add credential, lc - list credentials, dl - delete credential, ex - exit')
                    print('………')

                    shortCode = input().lower()
                    if shortCode == 'ac':
                        print('----------')
                        print('Save new credential...')
                        print('----------')
                        print('Enter account to save credentials for: ')
                        credAccount = input()
                        print('…')

                        print('Enter username: ')
                        credUserName = input()
                        print('…')

                        passResponse = input(
                            'Hello, do you neeed a generated password? \n  Respond with \'y\' for yes or \'n\' for no: ').lower()

                        if passResponse == 'y':
                            createdPass = passwordGenerator(getPassLength())
                            confirmedPass = createdPass

                            save_credentials(create_credentials(
                                credAccount, credUserName, createdPass))
                            print(
                                f'''
                                                New password successfully generated ({str(len(createdPass))}):  
                                                as shown below
                                                {createdPass}
                                                ''')
                        else:
                            print('Enter password: ')
                            credPass = input()

                            print('Comfirm password: ')
                            confirmedPass = input()

                            print('\n')

                            if credPass != confirmedPass:
                                print('Invalid: Passwords did not match!')
                                print('Enter password: ')
                                credPass = input()

                                print('Confirm password: ')
                                confirmedPass = input()
                            else:
                                save_credentials(create_credentials(
                                    credAccount, credUserName, credPass))
                                print(
                                    f'Your credentials for {credAccount} was successfully created!')
                                print('\n')

                    elif shortCode == 'lc':
                        if display_credentials():
                            print('Here is a list of all your Accounts with their data.')
                            print('\n')
                            for credential in display_credentials():
                                print(
                                    f'{credential.account}: \n user name: {credential.username}, password: {credential.password}')

                            print('\n')
                        else:
                            print('\n')
                            print("Sorry, you don't seem to have any data saved ")
                            print('\n')

                    elif shortCode == "dl":
                                        print("Enter the Username of the account you want to delete")
                                        username = input()
                                        if  check_existing_credentials(username):
                                            print("loading ...")
                                            username = find_credentials(username)
                                            delete_credentials(credential)
                                            print(
                                                f"Account {username.account} deleted successfully")
                                        else:
                                            print('\n')


                    elif shortCode == "ex": 
                                        print('Confirm that you want to exit password locker by navigating to exit again!!!')
                                        break

                    elif shortCode == 'ex':
                        break

                    else:
                     print('Invalid credentials short code')

        elif shortCode == 'ex':
            print('Thank you, and welcome again, have a great day!')
            break
if __name__ == '__main__':
    main()


