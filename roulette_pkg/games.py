import numpy as np
import random
import warnings
from roulette_pkg import table
warnings.simplefilter(action='ignore', category=FutureWarning)

# only game_table is necessary. delete and call game_table for wheel & board
game_table = table.RouletteTable()
wheel = game_table.roulette_wheel()
board = game_table.roulette_board()


class RouletteGames:
    def payout(self, cover, bet):
        return ((36-cover)/cover)*bet

    # checks for oversized bets and no user input
    def bet_amount(self, balance):
        while True:
            try:
                bet = float(input("Enter bet amount: $"))
                if bet <= 0.0:
                    print("Bet must be greater than 0.\n")
                elif bet > balance:
                    print(
                        f"\nYour bet is larger than your account of ${balance}.\nEnter a smaller bet.")
                else:
                    return bet
            except:
                print(f"\nEnter a number value.")

    # return coordinates of an element in the board matrix
    def find(self, element, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == element:
                    return (i, j)

    def number_check(self, number):
        if (0 <= int(number) <= 36) or number == "00":
            return True
        return False
    
    def bet_menu(self):
        return "*****BET MENU*****\n****INSIDE BETS***\n1. Straight Bet\n2. Split Bet\n3. Street Bet"\
            "\n4. Corner Bet\n5. Five Bet\n6. Line Bet\n\n****OUTSIDE BETS***\nHALF PAYOUT OF BET IF 0 or 00\n"\
            "\n7. Column Bet\n8. Dozen Bet\n9. Color Bet\n10. Even/Odd Bet\n11. Low/High Bet\n12. NewAR Bet\n"

    def straight_bet(self, balance):
        choice = ""
        while True:
            try:
                print(
                    "\nSTRAIGHT BET:\nPlace a bet on which number the pill will land on. (odds 35:1)\n")
                choice = input(
                    "\nEnter the number to bet on. \nValid numbers to bet on are 0-36 and '00': ")
                if self.number_check(choice):
                    break
            except ValueError:
                print(f"{choice} is invalid.")

        bet_amt = 0.0
        bet_amt = self.bet_amount(balance)

        spin = game_table.spin()
        print(f"The the pill landed on {spin} {wheel[spin]}!\n")

        if choice == spin:
            print(f"Straight bet on {choice} wins!!!\n")
            return 1, self.payout(1, bet_amt)
        else:
            print(f"Straight bet on {choice} is not a winner.\n")
            return 0, bet_amt

    def split_bet(self, balance):
        bet_amt = 0.0
        choice1 = ""
        choice2 = ""
        while True:
            game_table.display_board()
            try:
                print(
                    "\nSPLIT BET:\nPick two adjacent numbers. If pill lands on either number you win. (odds 17:1)\n")
                choice1 = input(
                    "\nEnter the first number to bet on. \nValid numbers to bet on are 0-36 and '00': ")
                choice2 = input(
                    "\nEnter the second number to bet on. \nValid numbers to bet on are 0-36 and '00': ")
                if self.number_check(choice1) and self.number_check(choice2):
                    print(f"\n{choice1} & {choice2} are valid.")
                    choice1_loc = self.find(choice1, board)
                    choice2_loc = self.find(choice2, board)
                    if (abs(choice1_loc[0] - choice2_loc[0]) + abs(choice1_loc[1] - choice2_loc[1])) == 1:
                        print(f"{choice1} & {choice2} are adjacent.\n")
                        while True:
                            bet_amt = self.bet_amount(balance)
                            spin = game_table.spin()
                            print(
                                f"The the ball stopped on {spin} {wheel[spin]}!\n")

                            if spin == choice1:
                                print(
                                    f"The split bet is a winner! {spin} = {choice1}")
                                return 1, self.payout(1, bet_amt)
                            if spin == choice2:
                                print(
                                    f"The split bet is a winner! {spin} = {choice2}")
                                return 1, self.payout(1, bet_amt)
                            if spin != choice1 and spin != choice2:
                                print(
                                    f"The split bet for {choice1} & {choice2} was not a winner.")
                                return 0, bet_amt
                    else:
                        print(
                            f"{choice1} & {choice2} are NOT adjacent. Enter numbers that share a border.\n")
                else:
                    print(f"{choice1} or {choice2} is NOT valid.")
            except ValueError:
                print(f"Enter valid numbers.")

    def corner_bet(self, balance):
        choice1 = ""
        choice2 = ""
        choice3 = ""
        choice4 = ""
        bet_amt = 0.0
        while True:
            game_table.display_board()
            try:
                print("\nCORNER BET:\nPick four numbers which touch at a corner.\nIf the pill lands on the number or any of the four numbers you win. (odds 8:1)\n")
                choice1 = input(
                    "Enter the first number the number to place the corner bet on. \nValid numbers to bet on are 1-36: ")
                choice2 = input(
                    "Enter the second number the number to place the corner bet on. \nValid numbers to bet on are 1-36: ")
                choice3 = input(
                    "Enter the third number the number to place the corner bet on. \nValid numbers to bet on are 1-36: ")
                choice4 = input(
                    "Enter the fourth number the number to place the corner bet on. \nValid numbers to bet on are 1-36: ")
                choices = [choice1, choice2, choice3, choice4]
                # check if elements are unique

                def dupe_check(lst):
                    for choice in lst:
                        if choices.count(choice) > 1:
                            return True
                    return False
                if self.number_check(choice1) and self.number_check(choice2) and self.number_check(choice3) and self.number_check(choice4):
                    # sort user input so choices are always in ascending order for diagonal check
                    picks = [choice1, choice2, choice3, choice4]
                    picks.sort(key=int)

                    # split coodrinate tuples into individual variables
                    p1X, p1Y = self.find(picks[0], board)
                    p2X, p2Y = self.find(picks[1], board)
                    p3X, p3Y = self.find(picks[2], board)
                    p4X, p4Y = self.find(picks[3], board)
                    # checking if elements are diagonal
                if (p4X-p4Y == p1X-p1Y or p4X + p4Y == p1X + p1Y) and (p2X-p2Y == p3X-p3Y or p2X+p2Y == p3X+p3Y):
                    print(
                        f"{choice1}, {choice2}, {choice3}, {choice4} are valid entries.")
                    if not(dupe_check(choices)):
                        break
                    else:
                        print(
                            f"The picks {choice1}, {choice2}, {choice3}, {choice4} contain duplicate values.\nPicks must be unique values.")
                else:
                    print(
                        f"{choice1}, {choice2}, {choice3}, {choice4} are INVALID entries.\nPicks must share a common corner on the board.")
            except ValueError:
                print(
                    f"\nOne ore more choices are invalid: {choice1}, {choice2}, {choice3}, {choice4}")

        bet_amt = self.bet_amount(balance)

        spin = game_table.spin()
        print(f"The the pill landed on {spin} {wheel[spin]}!\n")

        if str(spin) == choice1 or str(spin) == choice2 or str(spin) == choice3 or str(spin) == choice4:
            print(
                f"The corner bet is a winner! {spin} is one of your chosen numbers!")
            return 1, self.payout(4, bet_amt)
        else:
            print(
                f"The corner bet is NOT a winner. {spin} is not one of your chosen numbers {choice1}, {choice2}, {choice3}, or {choice4}.")
            return 0, bet_amt

    def street_bet(self, balance):

        sel_row = []
        choice = 0
        bet_amt = 0.0
        while True:
            game_table.display_board()
            for i in range(len(board)):
                print(f"{i+1}.) {board[i]}")
            try:
                print(
                    "\nSTREET BET:\nPlace a bet on which row of numbers the pill will land on. (odds 11:1)\n")
                choice = int(input("\nEnter choice: "))
                if not(choice > len(board) or choice < 1):
                    sel_row = board[choice-1]
                    break
                else:
                    print(f"The selected choice {choice} is out of range.")
            except ValueError:
                print(f"{choice} is invalid.")

        bet_amt = self.bet_amount(balance)

        spin = game_table.spin()
        print(f"The the pill landed on {spin} {wheel[spin]}!\n")

        if str(spin) in sel_row:
            print(
                f"You WIN!!!! {spin} is in your selected row {board[choice-1]}!!!!!\n")
            return 1, self.payout(3, bet_amt)
        else:
            print(
                f"You lose. {spin} is NOT in your selected row {board[choice-1]}\n")
            return 0, bet_amt

    def five_bet(self, balance):
        bet_amt = 0.0
        winning_numbers = ["00", "0", "1", "2", "3"]
        print(
            f"\nSUCKER BET (Five Bet):\nIf the pill lands on any of the numbers listed below you win. (odds 6:1)\nWinning numbers: {winning_numbers}\n")
        bet_amt = self.bet_amount(balance)

        spin = game_table.spin()
        print(f"The the pill landed on {spin} {wheel[spin]}!\n")

        if str(spin) in winning_numbers:
            print(f"You win!!!! The pill landed on {spin}!")
            return 1, self.payout(5, bet_amt)
        else:
            print(f"You lose. {spin} did NOT land on 00, 0, 1, 2, 3")
            return 0, bet_amt

    def line_bet(self, balance):
        bet_amt = 0.0
        row1 = []
        row2 = []
        choices = {
            1: ["You selected the numbers 1-6", 1, 2],
            2: ["You selected the numbers 7-12", 3, 4],
            3: ["You selected the numbers 13-18", 5, 6],
            4: ["You selected the numbers 19-24", 7, 8],
            5: ["You selected the numbers 25-30", 9, 10],
            6: ["You selected the numbers 31-36", 11, 12],
        }

        while True:
            game_table.display_board()
            print("\nLINE BET:\nSelect any two adjacent rows. If the pill lands on any number in the two selected rows you win. (odds 5:1)\n")
            print(
                "Available Bets:\n1. 1-6\n2. 7-12\n3. 13-18\n4. 19-24\n5. 25-30\n6. 31-36\n")
            try:
                choice = int(input("Enter selection: "))
                if 1 <= choice <= 12:
                    print(choices[choice][0])
                    row1 = list(board[choices[choice][1]])
                    row2 = list(board[choices[choice][2]])
                    break
                else:
                    print(f"{choice} is an invalid selection. Enter a number 1-6.")
            except (ValueError, KeyError):
                print(f"{choice} is not valid.")

        bet_amt = self.bet_amount(balance)

        spin = random.choice(list(wheel))
        print(f"The the ball stopped on {spin} {wheel[spin]}!\n")
        winNums = row1 + row2
        if str(spin) in winNums:
            print(f"You win!!!! The pill landed on {spin}!")
            pay = self.payout(6, bet_amt)
            return 1, pay
        else:
            print(f"You lose. {spin} did NOT land on {winNums}")
            return 0, bet_amt

    def column_bet(self, balance):
        choices = {
            1: ["You chose column 1", board[:, 0]],
            2: ["You chose column 2", board[:, 1]],
            3: ["You chose column 3", board[:, 2]]
        }
        bet_amt = 0.0
        col = []
        while True:
            game_table.display_board()
            print("\nCOLUMN BET:\nSelect a column of numbers. If the pill lands on a number of the selected column you win. (odds 2:1)\n")
            print(
                f"Select column: \n1. {choices[1][1]}\n2. {choices[2][1]}\n3. {choices[3][1]}\n")
            try:
                choice = int(input("Enter selection: "))
                if 1 <= choice <= 3:
                    col = choices[choice][1]
                    break
            except (ValueError, KeyError):
                print(f"{choice} is not valid.")

        bet_amt = self.bet_amount(balance)

        spin = random.choice(list(wheel))
        print(f"The the ball stopped on {spin} {wheel[spin]}!\n")

        if str(spin) == "0" or str(spin) == "00":
            print(f"The pill landed on {spin}. Your bet will be halved.")
            return 1, bet_amt/2
        elif str(spin) in col:
            print(f"You win!!!! The pill landed on {spin}!")
            pay = self.payout(12, bet_amt)
            return 1, pay
        else:
            print(f"You lose. {spin} did NOT land on {col}")
            return 0, bet_amt

    def dozen_bet(self, balance):
        bet_amt = 0.0
        dozen = []
        # flattened lists for each third of the playing board
        thirds = {
            1: [x for l in list(board[1:4]) for x in l],
            2: [x for l in list(board[5:9]) for x in l],
            3: [x for l in list(board[9:]) for x in l]
        }

        while True:
            game_table.display_board()
            print("\nDOZEN BET:\nSelect a dozen of numbers grouped by their board position. If the pill lands on a number of the selected dozen you win. (odds 2:1)\n")
            print(
                f"Select dozen: \n1. {thirds[1]}\n2. {thirds[2]}\n3. {thirds[3]}\n")
            try:
                choice = int(input("Enter selection: "))
                if 1 <= choice <= 3:
                    dozen = thirds[choice]
                    print(dozen)
                    break
            except (ValueError, KeyError):
                print(f"{choice} is not valid.")

        bet_amt = self.bet_amount(balance)

        spin = game_table.spin()
        print(f"The the pill landed on {spin} {wheel[spin]}!\n")

        if str(spin) == "0" or str(spin) == "00":
            print(f"The pill landed on {spin}. Your bet will be halved.")
            return 1, bet_amt/2
        elif str(spin) in dozen:
            print(f"You win!!!! The pill landed on {spin}!")
            pay = self.payout(12, bet_amt)
            return 1, pay
        else:
            print(f"You lose. {spin} did NOT land on {dozen}")
            return 0, bet_amt

    def oddeven_bet(self, balance):
        bet_amt = 0.0
        bet = ""
        while True:
            game_table.display_board()
            print("\nODD/EVEN BET:\nPlace a bet on whether the pill will land on an odd or even number. (odds 1:1)\n")
            print(f"Select bet: \n1. Odd\n2. Even\n")
            choice = input("Enter selection: ")
            bet_amt = self.bet_amount(balance)

            if choice == "1":
                print(f"You chose odd.")
                bet = "Odd"
                break
            elif choice == "2":
                print(f"You chose even.")
                bet = "Even"
                break
            else:
                print(f"{choice} is invalid. Enter a choice 1 or 2.")

        spin = game_table.spin()
        print(f"The the pill landed on {spin} {wheel[spin]}!\n")

        if str(spin) == "0" or str(spin) == "00":
            print(f"The pill landed on {spin}. Your bet will be halved.")
            return 1, bet_amt/2
        elif bet == "Odd":
            if (spin % 2) != 0:
                print(f"You win!!!! The pill landed on {wheel[spin]} odd!")
                return 1, self.payout(18, bet_amt)
            else:
                print(f"You lose. {spin} {wheel[spin]} was NOT odd")
                return 0, bet_amt
        elif bet == "Even":
            if (spin % 2) == 0:
                print(f"You win!!!! The pill landed on {wheel[spin]} even!")
                return 1, self.payout(18, bet_amt)
            else:
                print(f"You lose. {spin} {wheel[spin]} was NOT even")
                return 0, bet_amt

    def lohi_bet(self, balance):
        lowNums = [x for l in list(board[1:7]) for x in l]
        highNums = [x for l in list(board[7:]) for x in l]
        bet_amt = 0.0
        choice = ""
        while True:
            game_table.display_board()
            print("\nLOW/HIGH BET:\nPlace a bet on whether the pill will land on either the upper half or lower half of the numbers on the board. (odds 1:1)\n")
            print(f"Select bet: \n1. 1 - 18\n2. 19 - 36\n")
            choice = input("Enter selection: ")
            bet_amt = self.bet_amount(balance)

            if choice == "1":
                print(f"You chose low numbers (1-18).")
                choice = "low"
                break
            elif choice == "2":
                print(f"You chose high numbers (19-36).")
                choice = "high"
                break
            else:
                print(f"{choice} is invalid. Enter a choice 1 or 2.")

        spin = game_table.spin()
        print(f"The the ball stopped on {spin} {wheel[spin]}!\n")

        if str(spin) == "0" or str(spin) == "00":
            print(f"The pill landed on {spin}. Your bet will be halved.")
            return 1, bet_amt/2
        elif choice == "low":
            if str(spin) in lowNums:
                print(f"You win!!!! The pill landed on {spin}!")
                return 1, self.payout(18, bet_amt)
            else:
                print(
                    f"You lose. {spin} did NOT land on a number between 1-18")
                return 0, bet_amt
        elif choice == "high":
            if str(spin) in highNums:
                print(f"You win!!!! The pill landed on {spin}!")
                return 1, self.payout(18, bet_amt)
            else:
                print(
                    f"You lose. {spin} did NOT land on a number between 19-36")
                return 0, bet_amt

    def color_bet(self, balance):
        bet_amt = 0.0
        choice = ""
        while True:
            print("\COLOR BET:\nPlace a bet on whether the pill will land on number that is red or black. (odds 1:1)\n")
            print(f"Select bet: \n1. Black\n2. Red\n")
            choice = input("Enter selection: ")
            bet_amt = self.bet_amount(balance)

            if choice == "1":
                print(f"You chose black.")
                choice = "Black"
                break
            elif choice == "2":
                print(f"You chose red.")
                choice = "Red"
                break
            else:
                print(f"{choice} is invalid. Enter a choice 1 or 2.")

        spin = random.choice(list(wheel))
        print(f"The the ball stopped on {spin} {wheel[spin]}!\n")

        if choice == wheel[spin]:
            print(f"You win!!! The pill landed on {wheel[spin]}")
            return 1, self.payout(18, bet_amt)
        else:
            print(f"You lose. The pill landed on {wheel[spin]}.")
            return 0, bet_amt

    def newAr_bet(self, balance):
        bet_amt = 0.0
        bet = ""
        while True:
            game_table.display_board()
            print("\nNewAR BET:\nThere are three requirements for the bet.\n1. Color\n2. Odd/Even\n3. Number\nYou must bet on whether the pill will land on any of the above conditions.\n(odds 3:1. If pill lands on 0, odds 2:1)\n")
            print(f"Select bet: \n1. Black/Odd or 0\n2. Red/Even or 0\n")
            choice = input("Enter selection: ")
            bet_amt = self.bet_amount(balance)

            if choice == "1":
                print(f"You chose bet 1.")
                bet = choice
                break
            elif choice == "2":
                print(f"You chose bet 2.")
                bet = choice
                break
            else:
                print(f"{choice} is invalid. Enter a choice 1 or 2.")

        spin = game_table.spin()
        print(f"The the pill landed on {spin} {wheel[spin]}!\n")

        color = wheel[spin]
        oddEven = spin % 2 == 0 and "Even" or "Odd"
        isZero = spin == 0

        if bet == "1":
            if color == "Black" and oddEven == "Odd":
                print(
                    f"You win!!! NewAR requirements for {spin} {wheel[spin]} are met!\n")
                return 1, self.payout(3, bet_amt)
            elif isZero:
                print(
                    f"You win!!! The pill landed on {spin}! Your payout is now 2:1.\n")
                return 1, self.payout(12, bet_amt)
            else:
                print(
                    f"You lose. {spin} {wheel[spin]} does not meet the chosen NewAR requirements")
                return 0, bet_amt
        elif bet == "2":
            if color == "Red" and oddEven == "Even" or isZero == True:
                print(
                    f"You win!!! NewAR requirements for {spin} {wheel[spin]} are met!\n")
                return 1, self.payout(3, bet_amt)
            elif isZero:
                print(
                    f"You win!!! The pill landed on {spin}! Your payout is now 2:1.\n")
                return 1, self.payout(12, bet_amt)
            else:
                print(
                    f"You lose. {spin} {wheel[spin]} does not meet the chosen NewAR requirements")
                return 0, bet_amt

    
