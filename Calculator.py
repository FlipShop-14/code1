from tkinter import *

expression = ''

# Functions
def button_press(but):
    global expression
    # Check if the current expression already contains a decimal point
    if but == '.' and '.' in expression:
        return  # Avoid adding more than one decimal point
    expression += str(but)
    equation.set(expression)

def equals_but():
    try:
        global expression
        total = str(eval(expression))
        short_total = round(float(total), 3)
        equation.set(' ' + str(short_total))
        expression = str(short_total)
    except:
        equation.set('error')
        expression = ''

def clear():
    global expression
    expression = ''
    equation.set('0')

def cm_to_inches():
    try:
        global expression
        cm_value = float(expression)
        inch_value = cm_value * 0.393701
        inch_valueR = round(float(inch_value), 3)
        equation.set(' ' + str(inch_valueR))
        expression = str(inch_valueR)
    except ValueError:
        equation.set('error')
        expression = ''

def inches_to_cm():
    try:
        global expression
        inch_value = float(expression)
        cm_value = inch_value / 0.393701
        cm_valueR = round(float(cm_value), 3)
        equation.set(' ' + str(cm_valueR))
        expression = str(cm_valueR)
    except ValueError:
        equation.set('error')
        expression = ''

# Program window
window = Tk()
window.title("Calculator")
window.geometry("250x225")
window.config(bg="light blue")
window.resizable(False,False)

# Input/Output box
equation = StringVar()
expression_input = Entry(window, textvariable=equation)
expression_input.grid(row=0, column=0, columnspan=5, pady=5,ipady=4,ipadx=40)
expression_input.config(bg="yellow")
equation.set('0')

# Equation Buttons
plus = Button(window, text=" + ",width=4, command=lambda: button_press(" + "))
plus.grid(row=5, column=0,sticky=W, padx=5, pady=5)

minus = Button(window, text=" - ",width=4, command=lambda: button_press(" - "))
minus.grid(row=5, column=1)

divided = Button(window, text=" / ",width=4, command=lambda: button_press(" / "))
divided.grid(row=6, column=0,sticky=W, padx=5, pady=5 )

times = Button(window, text=" * ",width=4, command=lambda: button_press(" * "))
times.grid(row=6, column=1,sticky=W, padx=5, pady=5)

equals = Button(window, text=" = ",width=4, command=equals_but)
equals.grid(row=6, column=2,sticky=W, padx=5, pady=5)

dot = Button(window, text=" . ",width=4, command=lambda: button_press("."))
dot.grid(row=5, column=2,sticky=W, padx=5, pady=5)

# Number Buttons
but1 = Button(window, text=" 1 ",width=4, command=lambda: button_press("1"))
but1.grid(row=2, column=0,sticky=W, padx=5, pady=5)
but2 = Button(window, text=" 2 ",width=4, command=lambda: button_press("2"))
but2.grid(row=2, column=1,sticky=W, padx=5, pady=5)
but3 = Button(window, text=" 3 ",width=4, command=lambda: button_press("3"))
but3.grid(row=2, column=2,sticky=W, padx=5, pady=5)
but4 = Button(window, text=" 4 ",width=4, command=lambda: button_press("4"))
but4.grid(row=2, column=3)
but5 = Button(window, text=" 5 ",width=4, command=lambda: button_press("5"))
but5.grid(row=2, column=4,sticky=W, padx=5, pady=5)
but6 = Button(window, text=" 6 ",width=4, command=lambda: button_press("6"))
but6.grid(row=3, column=0,sticky=W, padx=5, pady=5)
but7 = Button(window, text=" 7 ",width=4, command=lambda: button_press("7"))
but7.grid(row=3, column=1,sticky=W, padx=5, pady=5)
but8 = Button(window, text=" 8 ",width=4, command=lambda: button_press("8"))
but8.grid(row=3, column=2,sticky=W, padx=5, pady=5)
but9 = Button(window, text=" 9 ",width=4, command=lambda: button_press("9"))
but9.grid(row=3, column=3,sticky=W, padx=6, pady=5)
but0 = Button(window, text=" 0 ",width=4, command=lambda: button_press("0"))
but0.grid(row=3, column=4,sticky=W, padx=5, pady=5)

# CM to Inches button
cmin_but = Button(window, text="CM/IN",width=4, command=cm_to_inches)
cmin_but.grid(row=7, column=3,sticky=W, padx=5, pady=5,ipady=2,ipadx=3)

# Inches to CM button
incm_but = Button(window, text="IN/CM",width=4, command=inches_to_cm)
incm_but.grid(row=7, column=4,sticky=W, padx=5, pady=5,ipady=2,ipadx=3)

# Clear button
clear_but = Button(window, text="C",width=4, command=clear)
clear_but.grid(row=7, column=0,sticky=W, padx=5, pady=5)

window.mainloop()