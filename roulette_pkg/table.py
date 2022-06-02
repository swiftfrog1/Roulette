import numpy as np
import random


class RouletteTable:

    def roulette_board(self):
        # American-style roulette board as a matrix
        board = np.array([
            ["Z", "0", "00"],
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["10", "11", "12"],
            ["13", "14", "15"],
            ["16", "17", "18"],
            ["19", "20", "21"],
            ["22", "23", "24"],
            ["25", "26", "27"],
            ["28", "29", "30"],
            ["31", "32", "33"],
            ["34", "35", "36"],
        ])
        return board

    def roulette_wheel(self):
        # American-style roulette wheel
        wheel = {
            00: "Green",
            27: "Red",
            10: "Black",
            25: "Red",
            29: "Black",
            12: "Red",
            8: "Black",
            19: "Red",
            31: "Black",
            18: "Red",
            6: "Black",
            21: "Red",
            33: "Black",
            16: "Red",
            4: "Black",
            23: "Red",
            35: "Black",
            14: "Red",
            2: "Black",
            0: "Green",
            28: "Black",
            9: "Red",
            26: "Black",
            30: "Red",
            11: "Black",
            7: "Red",
            20: "Black",
            32: "Red",
            17: "Black",
            5: "Red",
            22: "Black",
            34: "Red",
            15: "Black",
            3: "Red",
            24: "Black",
            36: "Red",
            13: "Black",
            1: "Red"
        }
        return wheel

    def display_board(self):
        print("\n*****************ROULETTE TABLE (American)*****************")
        print("   __________________________________________________________")
        print("  /   |   |   |   |   |   |   |   |   |   |   |   |   |      |")
        print(" /    | 3 | 6 | 9 | 12| 15| 18| 21| 24| 27| 30| 33| 36|  2:1 |")
        print("/ 00  |___|___|___|___|___|___|___|___|___|___|___|___|______|")
        print("\     |   |   |   |   |   |   |   |   |   |   |   |   |      |")
        print(" \____| 2 | 5 | 8 | 11| 14| 17| 20| 23| 26| 29| 32| 35|  2:1 |")
        print(" /    |___|___|___|___|___|___|___|___|___|___|___|___|______|")
        print("/  0  |   |   |   |   |   |   |   |   |   |   |   |   |      |")
        print("\     | 1 | 4 | 7 | 10| 13| 16| 19| 22| 25| 28| 31| 34|  2:1 |")
        print(" \____|___|___|___|___|___|___|___|___|___|___|___|___|______|")
        print("      |     1st12     |     2nd12     |     3rd12     |")
        print("      |_______________|_______________|_______________|")
        print("      | 1to18 | EVEN  |  RED  | BLACK |  ODD  |19to36 |")
        print("      |_______|_______|_______|_______|_______|_______|")

    def spin(self):
        new_spin = random.choice(list(self.roulette_wheel()))
        return new_spin
