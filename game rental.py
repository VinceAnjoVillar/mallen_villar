game_lib = { 
    "Donkey Kong" : { "quantity" : 3, "cost" : 2},
    "Super Mario Bros": {"quantity" : 5, "cost" : 3},
    "Tetris" : {"quantity" : 2, "cost" : 3}
}

user_inventory = {}
user_acc = {}

admin_user = "admin"
admin_pass = "password"

def main_menu():
    print('Game rental')
    print('1. View Available Games')
    print('2. Register User')
    print('3. Log In')
    print('4. Admin Log in')
    print(' 5. Exit')

    choice = int(input('What would you lke to do? '))

    if  choice == 1:
        view_games()
    elif choice == 2:
        register()
    elif choice == 3:
        log_in()
    elif choice == 4:
        admin_login()


def admin_login():
    print('ADMIN LOGIN')
    username= input('Enter username: ')
    password = input('Enter password: ')

    if username == admin_user and password == admin_pass:
        admin_menu()

    def admin_menu():
        print('ADMIN MENU')
        print('1. Add new games')
        print('2. Update cost')
        print('3. Update quantity')
        print('4. Log out ')

        choice = int(input('What would you like to do? '))

        if choice == 1:
            add_game()

    def add_game():
        


def view_games():
    print([game_lib])
    print()

    choice = input('Enter Y to return: ')
    if choice.lower() == 'y':
        main_menu()

def register():
    print('Register to access and rent games')
    username = input('Enter username: ')
    password = input('Enter password: ')
    balance = 0
    points = 0

    user_acc[username] = {'username' : username,
                          'password' : password,
                          'balance' : balance,
                          'points' : points}
    
    print(f'Welcome {username}')

    choice = input('Enter Y to conitinue and N to go back to menu: ')
    if choice.lower() == 'y':
        log_in()
    elif choice.lower() == 'n':
        main_menu()


def log_in():
    username = input('Enter username: ')
    password = input('Enter password: ')

    if username in user_acc[username]['username'] and password in user_acc[username]['password']:
        user_menu(username)
    else:
        username not in user_acc[username]['username'] and password not in user_acc[username]['password']
        log_in()


def user_menu(username):
    print('RENT A GAME!')
    print('1. Rent a game')
    print('2. Return a game')
    print('3. Top up')
    print('4. Check Inventory')
    print('5. Redeem points')
    print('6. Check points')
    print('7. Exit')

    choice = int(input('Enter choice:  '))
    if choice == 1:
        rent_game(username)
    elif choice == 2:
        retunr_game(username)
    elif choice == 3:
        top_up(username)
    elif choice == 4:
        check_inventory(username)
    elif choice == 5:
        redeem_points(username)
    elif choice == 6:
        checkpoints(username)
    elif choice == 7:
        main_menu()

def rent_game(username):
    while True:
        try:
            print('Rent a gam\n')
            print([game_lib])
            print()
        
            gamename = input('Enter game name to rent: ')
        
            if gamename in game_lib[gamename] and game_lib[gamename]['quantity'] > 0:
                if user_acc[username]['balance'] >= game_lib[gamename]['cost']:
                    game_lib[gamename]['quantity'] -= 1
                    user_acc[username]['balance'] -= game_lib[gamename]['cost']
                    user_acc[username]['points'] += 1
                    if username not in user_inventory:
                        user_inventory[username] = [gamename]
                    else:
                        user_inventory[username].append(gamename)
                        print(f'Game rented successfully, Remaining balance is {user_acc[username]["balance"]}\n')
                else:
                    print('Insufficient Funds')
            elif gamename in game_lib[gamename] and game_lib[gamename]['quantity'] <= 0:
                print('Game out of stock')
            else:
                print('Game out of stock')
        except ValueError as e:
            print('Wrong input\n')
            user_menu(username)

        choice = input('Enter A to rent again, Enter Y to return to menu: ')
        if choice.lower() == 'y':
            user_menu(usenrame)
        elif choice.lower() != 'a':
            print('Invalid Input\n')
            
def retunr_game():
    print('i')

def top_up(username):
    print('TOP UP FUNDS')

    newbalance = int(input('Enter Amount to top up: '))

    user_acc[username]['balance'] += newbalance

    print(f'Your new balance is: {user_acc[username]["balance"]}')

    choice = input('Enter y to return to menu: ')
    if choice.lower() == 'y':
        user_menu()

def check_inventory(username):
    print([user_inventory])
    print()

    choice = input('Enter y to return to menu: ')
    if choice.lower() == 'y':
        user_menu()
def redeem_points(username):
    print(user_acc[username]["points"])

    choice = input('Enter Y to redeem points and N to return to menu: ')
    if choice.upper() == 'Y':
        print('r')
    else:
        choice.lower() == 'N'
        user_menu()

def checkpoints(username):
    print(f'Available points: {user_acc[username]["points"]}\n')

    choice = input('Enter y to return to menu: ')
    if choice.lower() == 'y':
        user_menu()
main_menu()
