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
    print('5. Exit')

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
    elif choice == 2:
        game_name = input('Enter game to be updated.')
        if game_name in game_lib:
            new_price = int(input('Enter the new price of the game: '))
            game_lib[game_name]['cost'] = new_price
            print(f'Price succesfully updated. The new cost of {game_name} is {new_price}')
        else:
            print('Game not found in the system.')
            view_games()  
    elif choice == 3:
        game_name = input('Enter game to be updated.')
        if game_name in game_lib:
            new_quantity = int(input('Enter the new quantity of the game: '))
            game_lib[game_name]['quantity'] = new_quantity
            print(f'Quantity succesfully updated. The quantity of {game_name} is {new_quantity}')
        else:
            print('Game not found in the system')
            view_games()
    else:
        admin_menu()

def add_game():
    game_name = input('Enter the game name: ')
    quantity = int(input('Enter the quantity: '))
    cost = int(input('Enter the cost of the game: '))
    game_lib[game_name] = {'quantity' : quantity, 'cost' : cost}
    print(f'{game_name} added succesfully!')

    choice = input('Enter Y to return to menu: ')
    if choice.lower == 'y':
        admin_menu()
        
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
        
            if gamename in game_lib and game_lib[gamename]['quantity'] > 0:
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
            elif gamename in game_lib and game_lib[gamename]['quantity'] <= 0:
                print('Game out of stock')
            else:
                print('Invalid game selection')
        except ValueError as e:
            print('Wrong input\n')
            user_menu(username)

        choice = input('Enter A to rent again, Enter Y to return to menu: ')
        if choice.lower() == 'y':
            user_menu(username)
        elif choice.lower() != 'a':
            print('Invalid Input\n')
            
def retunr_game(username):
    while True:
        try:
            print('Return a game!')
            game_name = input('Enter the game you want to return: ')

            if game_name in user_inventory.get(username, []):
                user_inventory[username].remove(game_name)
                game_lib[game_name]['quantity'] += 1
                print(f'{game_name} returned succesfully')
            else:
                print('Game not found in user inventory')

        except ValueError as e:
            user_menu(username)

        choice = input('Press Y to return to menu. ')
        if choice.lower == 'y':
            user_menu(username)
            
def top_up(username):
    print('TOP UP FUNDS')

    newbalance = int(input('Enter Amount to top up: '))

    user_acc[username]['balance'] += newbalance

    print(f'Your new balance is: {user_acc[username]["balance"]}')

    choice = input('Enter y to return to menu: ')
    if choice.lower() == 'y':
        user_menu(username)

def check_inventory(username):
    while True:
        try:
            print()
            if username in user_inventory:
                print(f'Your inventory: {user_inventory[username]}\n')
            else:
                print('Inventory is Empty\n')

        except ValueError as e:
            user_menu(uername)

        choice = input('Press y to return to the main menu: ')
        if choice.lower() == 'y':
            return user_menu(username)
        
def redeem_points(username):
    while True:
        try:
            print()
            print('Redeem points\n')

            if user_Acc[username]['points'] >= 3:
                print('You can redeem your points to rent a game')
                choice = input('Do you want to redeem your points? (Y|N): ')
                if choice.lower() == 'y':
                    user_acc[username]['points'] -= 3
                    print('Points redeemed succefully!\n')
                    print(game_lib)
                    gamename = input('Select a game by typing the game name: ')
                    if gamename in game_lib and game_lib[gamename]['quantity'] > 0:
                        game_lib[gamename]['quantity'] -= 1
                        user_invebntory[username] = user_inventory.get(username, []) + [gamename]
                        print(f'Game "{gamename}" successfully rented\n')
                        return user_menu(uesrname)
                    else:
                        print('Invalid game selection or game is out of stock')
                        redeem_points(username)
                elif choice == 'n':
                    user_menu(username)
                else:
                    print('Invalid input. Please Enter Y or N')
                    redeem_points(username)
            else:
                print('Insufficient funds')
                redeem_points(username)
        except ValueError as e:
            usermenu(username)
        
def checkpoints(username):
    print(f'Available points: {user_acc[username]["points"]}\n')
    print('Enter Choice')
    print('1. Redeem points')
    print('2. Exit')
    
    choice = int(input('\nEnter Choice: '))
    if choice == 1:
        user_menu(username)
    elif choice == 2:
        return user_menu(usrname)
main_menu()
