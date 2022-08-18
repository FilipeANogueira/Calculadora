import tkinter as tk
from tkinter.constants import FLAT, LEFT, RIGHT
from factory import *

root = tk.Tk()

topLabel = tk.Label(root, bg="white", text="Sem conta ainda", anchor="e")
topLabel.grid(row=0, column=0, sticky="news", columnspan=5)

mainLabel = tk.Label(root, bg="white", text="", anchor="e")
mainLabel.grid(row=1, column=0, sticky="news", columnspan=5)

op = ""
def C():
    global op
    global n
    global n2
    op = ""
    n = ""
    n2 = ""
    mainLabel["text"] = ""
    topLabel["text"] = "Sem conta ainda"

def b0():
    if type(mainLabel["text"]) == float:
        C()
        mainLabel["text"] = mainLabel["text"]+"0"
    else:
        mainLabel["text"] = mainLabel["text"]+"0"

def b1():
    if type(mainLabel["text"]) == float:
        C()
        mainLabel["text"] = mainLabel["text"]+"1"
    else:
        mainLabel["text"] = mainLabel["text"]+"1"

def b2():
    if type(mainLabel["text"]) == float:
        C()
        mainLabel["text"] = mainLabel["text"]+"2"
    else:
        mainLabel["text"] = mainLabel["text"]+"2"

def b3():
    if type(mainLabel["text"]) == float:
        C()
        mainLabel["text"] = mainLabel["text"]+"3"
    else:
        mainLabel["text"] = mainLabel["text"]+"3"

def b4():
    if type(mainLabel["text"]) == float:
        C()
        mainLabel["text"] = mainLabel["text"]+"4"
    else:
        mainLabel["text"] = mainLabel["text"]+"4"

def b5():
    if type(mainLabel["text"]) == float:
        C()
        mainLabel["text"] = mainLabel["text"]+"5"
    else:
        mainLabel["text"] = mainLabel["text"]+"5"

def b6():
    if type(mainLabel["text"]) == float:
        C()
        mainLabel["text"] = mainLabel["text"]+"6"
    else:
        mainLabel["text"] = mainLabel["text"]+"6"

def b7():
    if type(mainLabel["text"]) == float:
        C()
        mainLabel["text"] = mainLabel["text"]+"7"
    else:
        mainLabel["text"] = mainLabel["text"]+"7"

def b8():
    if type(mainLabel["text"]) == float:
        C()
        mainLabel["text"] = mainLabel["text"]+"8"
    else:
        mainLabel["text"] = mainLabel["text"]+"8"

def b9():
    if type(mainLabel["text"]) == float:
        C()
        mainLabel["text"] = mainLabel["text"]+"9"
    else:
        mainLabel["text"] = mainLabel["text"]+"9"

def sum():
    global op
    global n
    op = "+"
    n = mainLabel["text"]
    topLabel["text"] = str(mainLabel["text"])+"+"
    mainLabel["text"] = ""  

def sub():
    global op
    global n
    op = "-"
    n = mainLabel["text"]
    topLabel["text"] = str(mainLabel["text"])+"-"
    mainLabel["text"] = ""

def div():
    global op
    global n
    op = "/"
    n = mainLabel["text"]
    topLabel["text"] = str(mainLabel["text"])+"/"
    mainLabel["text"] = ""

def multi():
    global op
    global n
    op = "*"
    n = mainLabel["text"]
    topLabel["text"] = str(mainLabel["text"])+"*"
    mainLabel["text"] = ""

def point():
    if type(mainLabel["text"]) == float:
        C()
        mainLabel["text"] = mainLabel["text"]+"."
    else:
        mainLabel["text"] = mainLabel["text"]+"."

def sqrt():
    global op
    op = sqrt
    topLabel["text"] = "√"

def expo():
    global op
    global n
    op = "^"
    n = mainLabel["text"]
    topLabel["text"] = str(mainLabel["text"])+"^"
    mainLabel["text"] = ""

def ANS():
    if type(mainLabel["text"]) == float:
        C()
        mainLabel["text"] = str(ans)
    elif type(mainLabel["text"]) == str:
        mainLabel["text"] = str(ans)

def equal():
    if type(mainLabel["text"]) != float:
        global n2
        global ans
        n2 = mainLabel["text"]
        topLabel["text"] = topLabel["text"]+str(mainLabel["text"])+"="
        mainLabel["text"] = ""
        if op == "":
            topLabel["text"] = n2+"="
            ans = float(n2)
        elif op == "+":
            ans = float(n) + float(n2)
        elif op == "-":
            ans = float(n) - float(n2)
        elif op == "/":
            ans = float(n) / float(n2)
        elif op == "*":
            ans = float(n) * float(n2)
        elif op == "^":
            ans = float(n) ** float(n2)
        elif op == sqrt:
            ans = float(n2) ** (1/2)
        mainLabel["text"] = ans
    else:
        C()

def on_click(event):
    if event.char == "1":
        b1()
    elif event.char == "2":
        b2()
    elif event.char == "3":
        b3()
    elif event.char == "4":
        b4()
    elif event.char == "5":
        b5()
    elif event.char == "6":
        b6()
    elif event.char == "7":
        b7()
    elif event.char == "8":
        b8()
    elif event.char == "9":
        b9()
    elif event.char == "+":
        sum()
    elif event.char == "-":
        sub()
    elif event.char == "/":
        div()
    elif event.char == "*":
        multi()
    elif event.char == "." or event.char == ",":
        point()

root.bind("<Key>", on_click)
root.bind("<Return>", lambda e: equal())
root.bind("<Delete>", lambda e: C())

butao = [("7", "8", "9", "/", "C"),
         ("4", "5", "6", "*", "+"),
         ("1", "2", "3", "^", "-"),
         (".", "0","ANS","√", "="),]

func = [( b7,   b8,  b9,  div,   C),
        ( b4,   b5,  b6,  multi, sum),
        ( b1,   b2,  b3,  expo,  sub),
        (point, b0, ANS,  sqrt,  equal)]

for (r, _) in enumerate(butao):
    for c, item in enumerate(butao[r]):
        button_function = func[r][c]
        if item == "C":
            factory.buttons(item, root, r+2, c, button_function, bg="red")
        elif item == "=":
            factory.buttons(item, root, r+2, c, button_function, bg="blue")
        else:
            factory.buttons(item, root, r+2, c, button_function)

root.config(bg="white")
root.title("Calculadora")
root.resizable(False, False)
root.mainloop()