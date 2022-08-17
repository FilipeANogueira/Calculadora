import tkinter as tk
from tkinter.constants import FLAT

class factory():
    def __init__(self, objeto):
        self.objeto = objeto

    def buttons(text:str, root, row, column, function, bg="white"):
        button = tk.Button(root, text=f"{text}", relief=FLAT, bg=bg, command=function)
        button.grid(row=row, column=column)
        button.config(padx=25, pady=20)

