#initialize the board with all blank spaces
def initialize_board(num_rows, num_cols):
    board = []
    for _ in range(num_rows):
        row = []
        for _ in range(num_cols):
            row.append("-")
        board.append(row)
    return board

#displays every column of every row in the board
def print_board(board):
    #iterates through the rows of board backwards to print board upside down
    for i in range(len(board)-1, -1, -1):
        row = board[i]
        for j in range(len(row)):
            if j == 0:
                print(board[i][j], end="")
            else:
                print(" " + board[i][j], end="")
        print()

#places a chip in the next available slot of the specified column
def insert_chip(board, col, chip_type):
    for i in range(len(board)):
        if board[i][col] == "-":
            board[i][col] = chip_type
            return i

#checks the board for a 4 in a row
def check_if_winner(board, col, row, chip_type):
    chips_together = 0
    #iterates through the row where the last chip was placed and checks for four in a row
    for j in range(len(board[row])):
        if board[row][j] == chip_type:
            chips_together += 1
            if chips_together == 4:
                return True
        else:
            chips_together = 0
    #iterates through the column where the last chip was placed and checks for four in a row
    chips_together = 0
    for i in range(len(board)):
        if board[i][col] == chip_type:
            chips_together += 1
            if chips_together == 4:
                return True
        else:
            chips_together = 0
    return False

def main():
    #initializes the game and size of board and tests for valid integer inputs
    num_rows = int(input("What would you like the height of the board to be? "))
    num_cols = int(input("What would you like the length of the board to be? "))
    total_chips = num_rows * num_cols
    board = initialize_board(num_rows, num_cols)
    print_board(board)
    print()
    print("Player 1: x")
    print("Player 2: o")
    print()

    #continue play until the board is full
    for _ in range(int(total_chips / 2)):
        #player 1's turn
        col = int(input("Player 1: Which column would you like to choose? "))
        row = insert_chip(board, col, "x")
        print_board(board)
        print()
        win = check_if_winner(board, col, row, "x")
        if win:
            print("Player 1 won the game!")
            quit()

        #player 2's turn
        col = int(input("Player 2: Which column would you like to choose? "))
        row = insert_chip(board, col, "o")
        print_board(board)
        print()
        win = check_if_winner(board, col, row, "o")
        if win:
            print("Player 2 won the game!")
            quit()

    #nobody won and the board is full
    print("Draw. Nobody wins.")
    quit()

if __name__ == "__main__":
    main()