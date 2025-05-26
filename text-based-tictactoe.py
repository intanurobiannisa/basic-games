# Function to print Tic Tac Toe
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

# Represents the Tic Tac Toe
values = [' ' for x in range(9)]
winner = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

cur_player = "O"
cur = []
# Function for a single game of Tic Tac Toe
player_pos = {'X': [], 'O': []}

is_game = True

while is_game:
    print_tic_tac_toe(values)

    if cur_player == 'X':
        cur_player = 'O'
    elif cur_player == 'O':
        cur_player = 'X'

    print("Player ",cur_player, " turn. Which box? : ", end="")
    move = int(input())
    cur.append(cur_player)
    # print(cur)
    # print(cur_player)

    player = str(cur[-1:]).replace("['", "").replace("']", "")

    # Sanity check for MOVE inout
    if move < 1 or move > 9:
        print("Wrong Input!!! Try Again")
        cur_player = player
        if cur_player == 'X':
            cur_player = 'O'
        elif cur_player == 'O':
            cur_player = 'X'
    # Check if the box is not occupied already
    elif values[move - 1] != ' ':
        print("Place already filled. Try again!!")
        cur_player = player
        if cur_player == 'X':
            cur_player = 'O'
        elif cur_player == 'O':
            cur_player = 'X'
    else:
        values[move - 1] = cur_player

        # Updating player positions
        player_pos[cur_player].append(move)
        # print(player_pos)

        # Check if the game is drawn
        if len(player_pos['X']) + len(player_pos['O']) == 9:
            print("the game is drawn")
            is_game = False

        # Check the winner
        for x in winner:
            if all(y in player_pos[cur_player] for y in x):
                print("Player ",cur_player, " is the winner.")
                print_tic_tac_toe(values)
                is_game = False
