# -----------------------------------------------------------------------------
# Name:       robot
# Purpose:    class definition for robots 
#
# Author:     Maksim Nikiforov
# Date:       11/06/2016
# -----------------------------------------------------------------------------

"""
Module to describe and control robot objects in a maze.
"""
import tkinter


class Robot(object):
    """
    Enter the class docstring here

    Arguments:
    list the arguments here (__init__'s arguments)

    Attributes:
    list ALL the attributes here (ALL the instance variables)
    """

    # class variable used by the show method
    unit_size = 60

    # Class variable describing the maze
    # False represents an obstacle, True represents open space
    maze = [[True, True, False, True, True, True, False, True, True, True],
           [True, True, False, True, True, True, False, True, True, True],
           [True, False, True, True, True, True, False, True, True, True],
           [True, True, True, True, True, True, True, True, False, True],
           [True, True, True, True, True, True, True, True, False, True],
           [True, True, True, True, True, True, True, True, True, True],
           [True, False, False, False, False, True, True, True, True, True],
           [True, True, False, True, True, True, True, True, False, True],
           [True, False, True, True, True, True, True, True, False, True],
           [True, True, True, True, True, True, True, True, False, True]]

    maze_size = len(maze)
    # class variable to represent a full charge
    # A robot with a fully charged battery can take up to 20 steps
    full = 20

    def __init__(self,  name, color, row=0, column=0):
        self.name = name
        self.color = color
        self.row = row
        self.column = column
        self.battery = self.full

    def __str__(self):
        return self.name + ' is a ' + self.color + ' lost in the maze.'

    def __gt__(self, other):
        if self.battery > other.battery:
            return True
        else:
            return False

    def recharge(self):
        """
         Recharge the robot's battery to the self.full class variable
        """
        self.battery = self.full

    def one_step_forward(self):
        """
        Enter the method's docstring here
        """
        if self.battery:
            self.column -= 1

    def one_step_back(self):
        """
        Enter the method's docstring here
        """
        if self.battery:
            self.column += 1

    def one_step_right(self):
        """
        Enter the method's docstring here
        """
        if self.battery:
            self.row -= 1

    def one_step_left(self):
        """
        Enter the method's docstring here
        """
        if self.battery:
            self.row -= 1

    def forward(self, steps):
        """
        Enter the method's docstring here
        """
        if self.battery:
            self.column -= steps

    def backward(self, steps):
        """
        Enter the method's docstring here
        """
        if self.battery:
            self.column += steps


    def right(self, steps):
        """
        Enter the method's docstring here
        """
        if self.battery:
            self.row += steps

    def left(self, steps):
        """
        Enter the method's docstring here
        """
        if self.battery:
            self.row -= steps

    # The method below has been written for you
    # You can use it when testing your class

    def show(self):
        """
        Draw a graphical representation of the robot in the maze.

        The robot's position and color are shown.
        The color is assumed to be one of the colors recognized by tkinter
        (https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm)
        If the robot's battery is empty, the robot is shown in a
        horizontal position. Otherwise the robot is shown in an upright
        position.
        The obstacles in the maze are shown in red.

        Parameter: None
        Return: None
        """
        root = tkinter.Tk()
        root.title (self.name + ' in the Maze')
        canvas= tkinter.Canvas(root, background = 'light green',
                               width = self.unit_size * self.maze_size,
                               height = self.unit_size * self.maze_size)
        canvas.grid()

        # draw a representation of the robot in the maze
        if self.battery:
            upper_x = self.column * self.unit_size + self.unit_size / 4
            upper_y = self.row * self.unit_size
            lower_x = upper_x + self.unit_size / 2
            lower_y = upper_y + self.unit_size
            eye_x = lower_x - 3 * self.unit_size /  20
            eye_y = upper_y + self.unit_size / 10

        else: # the robot ran out of battery
            upper_x = self.column * self.unit_size
            upper_y = self.row * self.unit_size + self.unit_size / 2
            lower_x = upper_x + self.unit_size
            lower_y = upper_y + self.unit_size / 2
            eye_x = lower_x - 9 * self.unit_size / 10
            eye_y = lower_y -  3 * self.unit_size / 20

        rectangle = canvas.create_rectangle(upper_x,
                                            upper_y,
                                            lower_x,
                                            lower_y,
                                            fill = self.color)
        # draw the robot's eyes
        canvas.create_oval(upper_x + self.unit_size / 10,
                           upper_y + self.unit_size / 10,
                           upper_x + 3 * self.unit_size / 20,
                           upper_y + 3 * self.unit_size / 20,
                           fill = 'black')
        canvas.create_oval(eye_x,
                           eye_y,
                           eye_x + self.unit_size / 20,
                           eye_y + self.unit_size / 20,
                           fill = 'black')
        # draw the obstacles in the maze
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                if not self.maze[row][col]:
                    canvas.create_rectangle(col * self.unit_size,
                                            row * self.unit_size,
                                            (col + 1) * self.unit_size,
                                            (row + 1) * self.unit_size,
                                            fill='red')
        for row in range(self.maze_size):
            canvas.create_line(0,
                               row * self.unit_size,
                               self.maze_size * self.unit_size,
                               row * self.unit_size)
        for col in range(self.maze_size):
            canvas.create_line(col * self.unit_size,
                               0,
                               col * self.unit_size,
                               self.maze_size * self.unit_size )
        root.mainloop()

def main():
