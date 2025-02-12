from tkinter import Button
import random
import settings

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
            
        )
        btn.bind('<Button-1>', self.left_click_action) #Button-1 = left click
        btn.bind('<Button-3>', self.right_click_action) #Button-3 = right click
        self.cell_btn = btn

    def left_click_action(self, event): #takes 2 parameters, 'event' gives some background information like the x and y location
        if self.is_mine:
            self.explode()
        else:
            self.reveal()

    def right_click_action(self, event): #takes 2 parameters, 'event' gives some background information like the x and y location
        print("RIGHT CLICKED!")


    def explode(self):
        #end the game
        self.cell_btn.configure(bg='red')

    @property #can be used as attribute
    def nearby_cells(self):
        #check surrounding cells for mines
        cells = [
            self.get_cell(self.x-1, self.y-1),
            self.get_cell(self.x-1, self.y),
            self.get_cell(self.x-1, self.y+1),
            self.get_cell(self.x, self.y-1),
            self.get_cell(self.x+1, self.y-1),
            self.get_cell(self.x+1, self.y),
            self.get_cell(self.x+1, self.y+1),
            self.get_cell(self.x, self.y+1),
        ]
        cells = [cell for cell in cells if cell is not None] #remove empty cells if the chosen cell is on the edge of the grid
        return cells

    @property
    def nearby_mines(self):
        count = 0
        for cell in self.nearby_cells:
            if cell.is_mine:
                count += 1
        return count

    def reveal(self):
        print(self.nearby_mines)

    def get_cell(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell  

    @staticmethod #doesn't belong to each instance but globally to the class
    def randomize_mines():
        mines = random.sample(Cell.all, settings.MINE_NUM) #obtains 25 random cells from the All list
        for mine in mines:
            mine.is_mine = True
    
    #when printing a cell, this formats it in a nice way "Cell(x, y)" instead of addresses 
    def __repr__(self) -> str:
        return f"Cell({self.x}, {self.y})"

