from tkinter import *
from typing import Collection
from PIL import ImageTk, Image
import webscraper

root = Tk()
root.title('Crypto Stats')
root.geometry('600x600')
title = Label(root, text="Crypto Info Gatherer").grid(row=0, column=1)
frame = LabelFrame(root, text="Your Mother", pady=200,padx=200, bg='white')
frame.grid(pady=50,padx=50, column=0,row=1, sticky='N', columnspan=3)
exit_button = Button(root, text='Exit', command=root.quit).grid(row=2, column=0)
info_button = Button(root, text='Info', command='').grid(row=2, column= 1)
holder_button = Button(root, text='Ino', command='').grid(row=2, column= 2)


label = Label(frame, text="Your Moth").pack()


root.mainloop()