import tictactoe
import numpy as np

class TicTacToeSolver:
    def __init__(self, game):
        self.game = game
        self.value_dict = {}
        self.action_dict = {}
        self.multiple_actions_dict = {}

    def solve(self):
        initial_state = self.game.get_initial_state()
        self.search_tictactoe_states(initial_state)

    def search_tictactoe_states(self, state):
        if state in self.value_dict:
            state_value = self.value_dict[state]
            return state_value

        if self.game.is_game_over(state):
            winner = self.game.get_winner(state, allow_draw = True)
            if winner is None:
                state_value = 0
            elif winner == state[0]:
                state_value = 1
            else:
                state_value = -1
            self.value_dict[state] = state_value
            return state_value
        
        else:
            best_action = None
            best_actions = []
            best_value = -1
            for action in self.game.get_legal_actions(state):
                
                next_state = self.game.get_next_state(state, action)
                next_value = -self.search_tictactoe_states(next_state)
                
                if best_action is None:
                    best_action = action
                    best_actions = [action]
                    best_value = next_value
                elif next_value > best_value:
                    best_action = action
                    best_actions = [action]
                    best_value = next_value
                elif next_value == best_value:
                    best_actions.append(action)
                
            self.value_dict[state] = best_value
            self.action_dict[state] = best_action
            
            self.multiple_actions_dict[state] = best_actions

            return best_value

if __name__ == "__main__":
    game = tictactoe.TicTacToeGame()
    solver = TicTacToeSolver(game)
    solver.solve()