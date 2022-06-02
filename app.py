from roulette_pkg import account
from roulette_pkg.games import RouletteGames
import sys
def start_game():
    while True:
        print("\n*****WELCOME TO ROULETTE (American-style)*****\n")
        player_name = input("Enter your name, or press enter to quit: ").capitalize()
        if player_name != "":
            acc = account.AccountInfo(0)
            acc.deposit()
            return player_name, acc
        elif player_name == "":
            print("Thanks for playing!!!")
            sys.exit()
        
def play_game(balance):
    rg = RouletteGames()
    print(rg.bet_menu())
    while True:
        try:
            choice = int(input("Enter a number 1 - 12: "))
            if 1 <= choice <= 12:
                if choice == 1:
                    return rg.straight_bet(balance)
                elif choice == 2:
                    return rg.split_bet(balance)
                elif choice == 3:
                    return rg.street_bet(balance)
                elif choice == 4:
                    return rg.corner_bet(balance)
                elif choice == 5:
                    return rg.five_bet(balance)
                elif choice == 6:
                    return rg.line_bet(balance)
                elif choice == 7:
                    return rg.column_bet(balance)
                elif choice == 8:
                    return rg.dozen_bet(balance)
                elif choice == 9:
                    return rg.color_bet(balance)
                elif choice == 10:
                    return rg.oddeven_bet(balance)
                elif choice == 11:
                    return rg.lohi_bet(balance)
                elif choice == 12:
                    return rg.newAr_bet(balance)  
        except ValueError:
            print("Invalid input. Try again")

def main_game(player, account):
    while True:
        start_balance = account.account_balance()
        print(f"\nHello {player}, your chip balance is: ${start_balance:.2f}\n")
        try:
            balance = account.account_balance()
            outcome, payout = play_game(balance)
        except UnboundLocalError as e:
            print(e)
        # outcome 1 is win
        if outcome == 1:
            account.win(payout)
            balance = account.account_balance()
            while True:
                print(balance)
                print("\n1. Play again\n2. Start new game\n3. Exit game")
                choice = input("Enter choice: ")
                if choice == "1":
                    main_game(player, account)
                elif choice == "2":
                    player, account = start_game()
                    main_game(player, account)
                elif choice == "3":
                    print(f"Thanks for playing {player}!")
                    sys.exit()
                else:
                    print(f"{choice} is invalid. Enter 1-3.")
        # outcome 0 is loss
        elif outcome == 0:
            account.loss(payout)
            balance = account.account_balance()
            if balance <= 0:
                print(f"Your account balance is {balance}!\n1. Add money\n2. New game\n3. Quit")
                selection = input("Enter choice: ")
                if selection == "1":
                    account.deposit()
                    main_game(player, account)
                elif selection == "2"         :
                    player, account = start_game()
                    main_game(player,account)
                elif selection == "3":
                    print(f"Thanks for playing {player}!!!\nEnding balance: ${balance}")
                    sys.exit()
            while True:
                print(balance)
                print("\n1. Play again\n2. Start new game\n3. Exit game")
                choice = input("Enter choice: ")
                if choice == "1":
                    main_game(player, account)
                elif choice == "2":
                    player, account = start_game()
                    main_game(player, account)
                elif choice == "3":
                    print(f"\nThanks for playing {player}!\nEnding balance: ${balance}")
                    sys.exit()
                else:
                    print(f"{choice} is invalid. Enter 1-3.")
    
new_player, new_account = start_game()
main_game(new_player, new_account)