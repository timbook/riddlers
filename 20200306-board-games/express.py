import numpy as np

class TicTacToeBoard:
    def distribute(self):
        self.board = np.random.permutation([
            "X", "X", "X", "X", "X",
            "O", "O", "O", "O"
        ]).reshape(3, 3)

    def check(self, sym):
        any_col = np.any([np.all(self.board[:, i] == sym) for i in range(3)])
        any_row = np.any([np.all(self.board[i, :] == sym) for i in range(3)])

        diag1 = np.all(
            np.array([self.board[0, 0], self.board[1, 1], self.board[2, 2]]) == sym
        )

        diag2 = np.all(
            np.array([self.board[0, 2], self.board[1, 1], self.board[2, 0]]) == sym
        )

        return any_col or any_row or diag1 or diag2

    def play(self):
        self.distribute()
        return self.check('X') and not self.check('O')

    def simulate(self, n):
        return np.mean(np.array([self.play() for _ in range(n)]))


b = TicTacToeBoard()
print('=== PROBABILITY OF X WINNING ===')
print(b.simulate(100_000))
