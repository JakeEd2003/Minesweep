from tkinter import Button

class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = False
        self.cell_btn = None

    def create_btn(self, location):
        btn = Button(
            location,
            text='Hello'
        )
        btn.bind('<Button-1>', self.left_click_action) #Button-1 = left click
        btn.bind('<Button-3>', self.right_click_action) #Button-3 = right click
        self.cell_btn = btn

    def left_click_action(self, event): #takes 2 parameters, 'event' gives some background information like the x and y location
        print("LEFT CLICKED!")

    def right_click_action(self, event): #takes 2 parameters, 'event' gives some background information like the x and y location
        print("RIGHT CLICKED!")

