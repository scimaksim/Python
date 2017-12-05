# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author:     Maksim Nikiforov
# -----------------------------------------------------------------------------
'''
Play a tic-tac-toe game against the computer.

The user always starts playing first.  The user marks a space on the grid by
clicking on that space.  That space is then colored with the user’s assigned
color. The computer immediately plays its move by coloring an available space
with the other color. The game goes on until one player
(the user or the computer) has 3 colored spaces in a line.
'''
import tkinter
import random


class Game(object):
    '''
    Represent an empty 3x3 tic-tac-toe board.

    Arguments:
    parent (string): name of GUI application main window

    Attributes:
    tile_size (integer): the size of each tile in pixels
    my_rectangles (set): a set of all rectangle identifiers which have been
                        filled by the user
    opp_rectangles (set): a set of all rectangle identifiers which have been
                        filled by the computer
    square_playable (bool): indicates whether squares can be clicked ('False'
                            in case of a win, loss, or a tie)
    '''

    tile_size = 100
    my_squares = set()
    opp_squares = set()
    square_playable = True
    # Define winning square ID combinations for squares on the board
    winning_streak = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7},
                      {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]

    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent

        # Create the restart button widget
        self.restart_button = tkinter.Button(self.parent, text='Restart',
                                        command=self.restart)
        self.restart_button.grid()

        # Create a canvas widget
        self.canvas = tkinter.Canvas(self.parent,
                                     width=self.tile_size * 3,
                                     height=self.tile_size * 3)
        self.canvas.grid()

        # Create the white tic-tac-toe tiles (3x3 board)
        for row in range(3):
            for column in range(3):
                color = 'white'
                self.canvas.create_rectangle(self.tile_size * column,
                                             self.tile_size * row,
                                             self.tile_size * (column + 1),
                                             self.tile_size * (row + 1),
                                             fill=color)

        # Create a label widget for the win/lose message
        self.win_lose = tkinter.Label(self.parent, text='...')
        self.win_lose.grid()

        # Bind a single click to the play function
        self.canvas.bind("<Button-1>", self.play)

    def restart(self):
        """
        Restarts the game when the "restart" button is clicked

        Parameter:

        Returns:

        """
        # This method is invoked when the user clicks on the RESTART button.
        # Reset clicked rectangle sets to 0 and make squares playable again
        self.my_squares = set()
        self.opp_squares = set()
        self.square_playable = True
        self.win_lose.configure(text='...')

        # Obtain list of all squares on the canvas and change color to white
        all_squares = self.canvas.find_all()
        for square in all_squares:
            self.canvas.itemconfig(square, fill='white')

    def play(self, event):
        """
        After a user clicks on a tile, determine which tile was clicked and
        fill it if possible. Allow the computer to make the subsequent move.

        Parameter:
        event (object): has details about an event (here, event is a click)
        Returns:

        """
        # This method is invoked when the user clicks on a square
        # If a game is in progress, allow square to be clicked
        if self.square_playable:
            # Find the square nearest to the click coordinates
            my_square = self.canvas.find_closest(event.x, event.y)[0]
            # Check if square has been previously clicked
            if my_square not in self.my_squares \
                    and my_square not in self.opp_squares:
                # If the square is not in use's clicked square set and not in
                # the opponent's clicked square set, color the square
                self.canvas.itemconfigure(my_square, fill='blue')
                # Add the square ID to the set of all squares that
                # the human user has played
                self.my_squares.add(my_square)

                # If an empty square is available to the computer, allow the
                # computer to make a move
                if len(self.my_squares) + len(self.opp_squares) < 8:
                    opponent_turn = True

                    while opponent_turn:
                        # Generate a random 'x' and 'y' coordinate within the
                        # confines of the canvas. Use the random pair to find
                        # the nearest square
                        rand_x = random.randint(0, self.canvas.winfo_height())
                        rand_y = random.randint(0, self.canvas.winfo_width())
                        opp_rectangle = self.canvas.find_closest(rand_x,
                                                                 rand_y)[0]
                        # If the nearest square has not been filled, allow the
                        # computer to fill it (and mark 'opponent_turn' False).
                        # Otherwise, generate another x-y combination
                        if opp_rectangle not in self.my_squares \
                                and opp_rectangle not in self.opp_squares:
                            self.canvas.itemconfigure(opp_rectangle,
                                                      fill='orange')
                            # Add the square ID to the set of all squares that
                            # the computer has played
                            self.opp_squares.add(opp_rectangle)
                            opponent_turn = False
                else:
                    # If the game reaches the last possible turn, declare the
                    # game a tie (checks for winner/loser are done below)
                    self.win_lose.configure(text='It\'s a tie!')
                    self.square_playable = False

            # Begin checking for winner/loser after 3 moves
            if len(self.my_squares) >= 3:
                # Compare the sets of user and computer moves to the sets of
                # winning combinations. If a winning combination is a subset of
                # moves made, declare the winner.
                for sets in self.winning_streak:
                    if sets.issubset(self.my_squares):
                        self.win_lose.configure(text='You win!')
                        self.square_playable = False
                    elif sets.issubset(self.opp_squares):
                        self.win_lose.configure(text='You lose!')
                        self.square_playable = False


def main():
    # Instantiate a root window
    root = tkinter.Tk()
    # Instantiate a Game object
    my_game = Game(root)
    # Enter the main event loop
    root.mainloop()


if __name__ == '__main__':
    main()
