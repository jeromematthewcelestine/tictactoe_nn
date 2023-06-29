import random

class TicTacToeGame():
    def __init__(self):
        pass

    def print_state(self, state):
        board = state[1]
        print(f' {board[0]} | {board[1]} | {board[2]} ')
        print('---+---+---')
        print(f' {board[3]} | {board[4]} | {board[5]} ')
        print('---+---+---')
        print(f' {board[6]} | {board[7]} | {board[8]} ')
        player = state[0]
        print(f'Player {player}\'s turn'    )

    def get_initial_state(self):
        player = 0
        board = (0, 0, 0, 0, 0, 0, 0, 0, 0)
        return (player, board)
    
    def get_legal_actions(self, state):
        board = state[1]
        legal_actions = []
        for i in range(9):
            if board[i] == 0:
                legal_actions.append(i)
        return legal_actions
    
    def get_player(self, state):
        return state[0]
    
    def get_winner(self, state, allow_draw = False):
        board = state[1]

        # rows
        if board[0] == board[1] == board[2] != 0:
            return board[0] - 1
        if board[3] == board[4] == board[5] != 0:
            return board[3] - 1
        if board[6] == board[7] == board[8] != 0:
            return board[6] - 1
        
        # columns
        if board[0] == board[3] == board[6] != 0:
            return board[0] - 1
        if board[1] == board[4] == board[7] != 0:
            return board[1] - 1
        if board[2] == board[5] == board[8] != 0:
            return board[2] - 1
        
        # diagonals
        if board[0] == board[4] == board[8] != 0:
            return board[0] - 1
        if board[2] == board[4] == board[6] != 0:
            return board[2] - 1
        
        if all(board[i] != 0 for i in range(9)):
            if allow_draw:
                return None
            else:
                return random.choice([0, 1])

        return None
    
    def is_game_over(self, state):
        return self.get_winner(state) is not None
    
    def get_next_state(self, state, action):
        
        player = state[0]
        board = state[1]
        board = list(board)
        board[action] = player + 1
        player = 1 - player
        return (player, tuple(board))

if __name__ == "__main__":
    game = TicTacToeGame()
    board, player = game.get_initial_state()
    while True:
        print('---')
        print(f'Player {player}\'s turn')
        print(board)
        print('Legal actions:', game.get_legal_actions((board, player)))
        action = int(input('Action: '))
        board, player = game.get_next_state((board, player), action)
        winner = game.get_winner((board, player))
        if winner is not None:
            print('---')
            print(f'Player {winner} wins!')
            print(board)
            break

