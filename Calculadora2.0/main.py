import tkinter as tk
from tkinter.constants import FLAT, LEFT, RIGHT
from factory import *

# def cria_func(botao):
#     return lambda label: print(botao)
def b0():
    mainLabel["text"] = mainLabel["text"]+"0"

def b1():
    mainLabel["text"] = mainLabel["text"]+"0"

def b2():
    mainLabel["text"] = mainLabel["text"]+"0"

def b3():
    mainLabel["text"] = mainLabel["text"]+"0"

def b4():
    mainLabel["text"] = mainLabel["text"]+"0"

def b5():
    mainLabel["text"] = mainLabel["text"]+"0"

def b6():
    mainLabel["text"] = mainLabel["text"]+"0"

def b7():
    mainLabel["text"] = mainLabel["text"]+"0"

def b8():
    mainLabel["text"] = mainLabel["text"]+"0"

def b9():
    mainLabel["text"] = mainLabel["text"]+"0"

def DEL():
    mainLabel["text"] = mainLabel["text"]+"0"

def C():
    mainLabel["text"] = mainLabel["text"]+"0"

def sum():
    mainLabel["text"] = mainLabel["text"]+"0"

def sub():
    mainLabel["text"] = mainLabel["text"]+"0"

def div():
    mainLabel["text"] = mainLabel["text"]+"0"

def multi():
    mainLabel["text"] = mainLabel["text"]+"0"

def point():
    mainLabel["text"] = mainLabel["text"]+"0"

def paren():
    mainLabel["text"] = mainLabel["text"]+"0"

def equal():
    mainLabel["text"] = mainLabel["text"]+"0"

def expo():
    mainLabel["text"] = mainLabel["text"]+"0"

root = tk.Tk()

topLabel = tk.Label(root, bg="white", text="Sem conta ainda", anchor="e")
topLabel.grid(row=0, column=0, sticky="news", columnspan=5)

mainLabel = tk.Label(root, bg="white", text="", anchor="e")
mainLabel.grid(row=1, column=0, sticky="news", columnspan=5)

butao = [("7", "8", "9", "DEL", "C"),
         ("4", "5", "6", "*", "/"),
         ("1", "2", "3", "+", "-"),
         ("(", "0", ".", "^", "="),]

func = [( b7,   b8,  b9,   DEL,   C),
        ( b4,   b5,  b6,  multi,  div),
        ( b1,   b2,  b3,   sum,   sub),
        (paren, b0, point, expo,  equal)]

for (r, _) in enumerate(butao):
    for c, item in enumerate(butao[r]):
        button_function = func[r][c]
        if item == "C" or item=="DEL":
            factory.buttons(item, root, r+2, c, button_function, bg="red")
        elif item == "=":
            factory.buttons(item, root, r+2, c, button_function, bg="blue")
        else:
            factory.buttons(item, root, r+2, c, button_function)

root.config(bg="white")
root.title("Calculadora")
root.resizable(False, False)
root.mainloop()