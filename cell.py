from tkinter import Button
import random

class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = False
        self.x = x
        self.y = y
        self.cell_btn = None

        #add cells to the list of all cells
        Cell.all.append(self)
        

    def create_btn(self, location):
        btn = Button(
            location,
            width=10,
            height=3,
            text=f"{self.x},{self.y}"
        )
        btn.bind('<Button-1>', self.left_click_action) #Button-1 = left click
        btn.bind('<Button-3>', self.right_click_action) #Button-3 = right click
        self.cell_btn = btn

    def left_click_action(self, event): #takes 2 parameters, 'event' gives some background information like the x and y location
        print("LEFT CLICKED!")

    def right_click_action(self, event): #takes 2 parameters, 'event' gives some background information like the x and y location
        print("RIGHT CLICKED!")

    @staticmethod #doesn't belong to each instance but globally to the class
    def randomize_mines():
        mines = random.sample(Cell.all, 25) #obtains 25 random cells from the All list
        for mine in mines:
            mine.is_mine = True
    
    #when printing a cell, this formats it in a nice way "Cell(x, y)" instead of addresses 
    def __repr__(self) -> str:
        return f"Cell({self.x}, {self.y})"

