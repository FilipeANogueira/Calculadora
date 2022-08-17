import tkinter as tk
import re

class principal():
    def __init__(self):
        
        root = tk.Tk()

        label= tk.Label(root, text="Sem conta ainda", bg="white", anchor="e")       # Label superior
        label.grid(column=0,row=0, columnspan=5, sticky="news")                     # Posicionamento
        label.config(justify="right")                                               # Configurações

        bot_label = tk.Label(root, bg="white", anchor="e")                          # Label inferior 
        bot_label.grid(column=0, row=1, columnspan=5, sticky="news")                # Posicionamento
        bot_label.config(justify="right",font=("Helvetica", 20, "bold"), bd=1)      # Configurações
        

        def click7():                                                                       # Função do botão 7
            if type(bot_label["text"]) == float:                                            # Análisando se ja foi feita uma conta anteriormente
                Clear()
                bot_label["text"] = bot_label["text"]+"7"
            else:
                bot_label["text"] = bot_label["text"]+"7"

        btn_7 = tk.Button(root, bg="#f1f2f3", text="7", command=click7)                     # Botão 7
        btn_7.grid(column=0, row=2, padx=0, pady=0)                                         # Posicionamento
        btn_7.config(font=("Helvetica", 15, "normal"),pady=18, padx=28, width=1, bd=0)      # Configurações

        def click8():                                                                       # Função do botão 8
            if type(bot_label["text"]) == float:                                            # Análisando se ja foi feita uma conta anteriormente                          
                Clear()
                bot_label["text"] = bot_label["text"]+"8"
            else:
                bot_label["text"] = bot_label["text"]+"8"

        btn_8 = tk.Button(root, bg="#f1f2f3", text="8", command=click8)                     # Botão 8
        btn_8.grid(column=1, row=2, padx=0, pady=0)                                         # Posicionamento
        btn_8.config(font=("Helvetica", 15, "normal"),pady=18, padx=28, width=1, bd=0)      # Configurações

        def click9():                                                                       # Função do botão 9
            if type(bot_label["text"]) == float:                                            # Análisando se ja foi feita uma conta anteriormente
                Clear()
                bot_label["text"] = bot_label["text"]+"9"
            else:
                bot_label["text"] = bot_label["text"]+"9"

        btn_9 = tk.Button(root, bg="#f1f2f3", text="9", command=click9)                     # Botão 9
        btn_9.grid(column=2, row=2, padx=0, pady=0)                                         # Posicionamento
        btn_9.config(font=("Helvetica", 15, "normal"),pady=18, padx=28, width=1, bd=0)      # Configurações

        def clickplus():                                                                    # Função do botão "-" menos
            global op                                                                       # Variáveis criadas e globalizadas ao executar a função
            global n
            op = "+"
            n = bot_label["text"]                                                           # Primeiro número
            label["text"] = str(bot_label["text"])+"+"                                      # Concatenação do primeiro número e "+"
            bot_label["text"] = ""          

        btn_plus = tk.Button(root, bg="#f1f2f3", text="+", command=clickplus)               # Botão "+" mais
        btn_plus.grid(column=3, row=2, padx=0, pady=0)                                      # Posicionamento
        btn_plus.config(font=("Helvetica", 15, "normal"),pady=18, padx=28, width=1, bd=0)   # Configurações

        def Clear():                                                                        # Função do botão "C" Clear
            global op                                                                       # Variáveis criadas e globalizadas ao executar a função
            global n
            global n2
            op = ""                                                                         # 
            n = ""
            n2 = ""
            bot_label["text"] = ""
            label["text"] = "Sem conta ainda"
        Clear()

        btn_c = tk.Button(root, bg="#f54b42", text="C", command = Clear)
        btn_c.grid(column=4, row=2, padx=0, pady=0)
        btn_c.config(font=("Helvetica", 15, "normal"),pady=18, padx=28, width=1, bd=0)

        def click4():
            if type(bot_label["text"]) == float:
                Clear()
                bot_label["text"] = bot_label["text"]+"4"
            else:
                bot_label["text"] = bot_label["text"]+"4"

        btn_4 = tk.Button(root, bg="#f1f2f3", text="4", command=click4)
        btn_4.grid(column=0, row=3, padx=0, pady=0)
        btn_4.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def click5():
            if type(bot_label["text"]) == float:
                Clear()
                bot_label["text"] = bot_label["text"]+"5"
            else:
                bot_label["text"] = bot_label["text"]+"5"

        btn_5 = tk.Button(root, bg="#f1f2f3", text="5", command=click5)
        btn_5.grid(column=1, row=3, padx=0, pady=0)
        btn_5.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def click6():
            if type(bot_label["text"]) == float:
                Clear()
                bot_label["text"] = bot_label["text"]+"6"
            else:
                bot_label["text"] = bot_label["text"]+"6"

        btn_6 = tk.Button(root, bg="#f1f2f3", text="6", command=click6)
        btn_6.grid(column=2, row=3, padx=0, pady=0)
        btn_6.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def clickminus():
            global op
            global n
            op = "-"
            n = bot_label["text"]
            label["text"] = str(bot_label["text"])+"-"
            bot_label["text"] = ""

        btn_minus = tk.Button(root, bg="#f1f2f3", text="-", command=clickminus)
        btn_minus.grid(column=3, row=3, padx=0, pady=0)
        btn_minus.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def clickdiv():
            global op
            global n
            op = "/"
            n = bot_label["text"]
            label["text"] = str(bot_label["text"])+"/"
            bot_label["text"] = ""

        btn_div = tk.Button(root, bg="#f1f2f3", text="/", command=clickdiv)
        btn_div.grid(column=4, row=3, padx=0, pady=0)
        btn_div.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def click1():
            if type(bot_label["text"]) == float:
                Clear()
                bot_label["text"] = bot_label["text"]+"1"
            else:
                bot_label["text"] = bot_label["text"]+"1"

        btn_1 = tk.Button(root, bg="#f1f2f3", text="1", command=click1)
        btn_1.grid(column=0, row=4, padx=0, pady=0)
        btn_1.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def click2():
            if type(bot_label["text"]) == float:
                Clear()
                bot_label["text"] = bot_label["text"]+"2"
            else:
                bot_label["text"] = bot_label["text"]+"2"

        btn_2 = tk.Button(root, bg="#f1f2f3", text="2", command=click2)
        btn_2.grid(column=1, row=4, padx=0, pady=0)
        btn_2.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def click3():
            if type(bot_label["text"]) == float:
                Clear()
                bot_label["text"] = bot_label["text"]+"3"
            else:
                bot_label["text"] = bot_label["text"]+"3"

        btn_3 = tk.Button(root, bg="#f1f2f3", text="3", command=click3)
        btn_3.grid(column=2, row=4, padx=0, pady=0)
        btn_3.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def clickx():
            global op
            global n
            op = "*"
            n = bot_label["text"]
            label["text"] = str(bot_label["text"])+"*"
            bot_label["text"] = ""

        btn_x = tk.Button(root, bg="#f1f2f3", text="*", command=clickx)
        btn_x.grid(column=3, row=4, padx=0, pady=0)
        btn_x.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def clickex():
            global op
            global n
            op = "^"
            n = bot_label["text"]
            label["text"] = str(bot_label["text"])+"^"
            bot_label["text"] = ""

        btn_ex = tk.Button(root, bg="#f1f2f3", text="^", command=clickex)
        btn_ex.grid(column=4, row=4, padx=0, pady=0)
        btn_ex.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def click0():
            if type(bot_label["text"]) == float:
                Clear()
                bot_label["text"] = bot_label["text"]+"0"
            else:
                bot_label["text"] = bot_label["text"]+"0"

        btn_0 = tk.Button(root, bg="#f1f2f3", text="0", command=click0)
        btn_0.grid(column=0, row=5, padx=0, pady=0)
        btn_0.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def clickpoint():
            bot_label["text"] = bot_label["text"]+"."

        btn_point = tk.Button(root, bg="#f1f2f3", text=".", command=clickpoint)
        btn_point.grid(column=1, row=5, padx=0, pady=0)
        btn_point.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def answer():
            if type(bot_label["text"]) == float:
                Clear()
                bot_label["text"] = str(ans)
            elif type(bot_label["text"]) == str:
                bot_label["text"] = str(ans)


        btn_a_parenteses = tk.Button(root, bg="#f1f2f3", text="Ans", command=answer)
        btn_a_parenteses.grid(column=2, row=5, padx=0, pady=0)
        btn_a_parenteses.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def sqrt():
            global op
            op = sqrt
            label["text"] = "√"

        btn_f_parenteses = tk.Button(root, bg="#f1f2f3", text="√", command=sqrt)
        btn_f_parenteses.grid(column=3, row=5, padx=0, pady=0)
        btn_f_parenteses.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        def entry_to_label():
            if type(bot_label["text"]) != float:
                global n2
                global ans
                n2 = bot_label["text"]
                label["text"] = label["text"]+str(bot_label["text"])+"="
                bot_label["text"] = ""
                if op == "":
                    label["text"] = n2+"="
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
                bot_label["text"] = ans
            else:
                Clear()
            
        

        def on_click(event):
            if event.char == "1":
                click1()
            elif event.char == "2":
                click2()
            elif event.char == "3":
                click3()
            elif event.char == "4":
                click4()
            elif event.char == "5":
                click5()
            elif event.char == "6":
                click6()
            elif event.char == "7":
                click7()
            elif event.char == "8":
                click8()
            elif event.char == "9":
                click9()
            elif event.char == "+":
                clickplus()
            elif event.char == "-":
                clickminus()
            elif event.char == "/":
                clickdiv()
            elif event.char == "*":
                clickx()
            elif event.char == ".":
                clickpoint()
            
        
        root.bind("<Key>", on_click)
        root.bind("<Return>", lambda e: entry_to_label())
        root.bind("<Delete>", lambda e: Clear())
                
             

        btn_equal = tk.Button(root, bg="#3a7efc", text="=", command=entry_to_label)
        btn_equal.grid(column=4, row=5, padx=0, pady=0)
        btn_equal.config(font=("Helvetica", 15, "normal"), pady=18, padx=28, width=1, bd=0)

        root.bind()

        root.resizable(False,False)
        root.title("Calculadora")
        root.config(padx=10, pady=10, bg="white")
        root.mainloop()
principal()