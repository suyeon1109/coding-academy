from ast import Expression
from tkinter import * #=library에서 책을 꺼내오는 / tkinter 라는 소스코드의 모든 기능을 가져오겠디.(오픈소스)

win =  Tk()
win.geometry("312x324") #가로 312 픽셀, 세로 324 픽셀로 창을 만들겠다
win.resizable(0, 0) #유저가 창을 늘리고 줄이는걸 방지
win.title("Calculator Made by Suyeon")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    expression = ""

expression = ""
input_text = StringVar()

input_frame = Frame(win, width=312, height=50, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

input_field =  Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) #internal padding(공간) 10 

btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()

#first row
clear = Button(btns_frame, text = "C", fg = "black", width=22, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text = "/", fg = "black", width=5, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

#second row
seven = Button(btns_frame, text = "7", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("7")).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text = "8", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("8")).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text = "9", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("9")).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text = "*", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

#third row
four = Button(btns_frame, text = "4", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click()).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text = "5", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click()).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text = "6", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click()).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text = "-", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click()).grid(row=2, column=3, padx=1, pady=1)

#fourth row
one = Button(btns_frame, text = "1", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click()).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text = "2", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click()).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text = "3", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click()).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text = "+", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click()).grid(row=3, column=3, padx=1, pady=1)

#fifth row
zero = Button(btns_frame, text = "0", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click()).grid(row=4, column=0, padx=1, pady=1)
point = Button(btns_frame, text = ".", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click()).grid(row=4, column=1, padx=1, pady=1)
equals = Button(btns_frame, text = "=", fg = "black", width=5, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: bt_equal()).grid(row=4, column=2, padx=1, pady=1)


win.mainloop()