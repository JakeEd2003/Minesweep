from tkinter import *
import settings
import utility

#initialize window and set colour, size and title
root = Tk() 
root.configure(background='azure1')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper") 
root.resizable(False, False)

#create a frame for the title
title_frame = Frame(
    root,
    bg='green',  #CHANGE LATER
    width=settings.WIDTH, 
    height=utility.height_prct(25)
)
title_frame.place(x=0, y=0)

#create left frame
left_frame = Frame(
    root,
    bg='red', #CHANGE LATER
    width=utility.width_prct(25),
    height=utility.height_prct(75)
)
left_frame.place(x=0, y=utility.height_prct(25))

#create main frame for game
game_frame = Frame(
    root,
    bg='blue', #CHANGE LATER
    width=utility.width_prct(75),
    height=utility.height_prct(75)
)
game_frame.place(x=utility.width_prct(25), y=utility.height_prct(25))

root.mainloop()