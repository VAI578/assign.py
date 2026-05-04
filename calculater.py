from tkinter import *

# Create window
root = Tk()
root.title("Calculator")

# Global variables
num1 = 0
operator = ""

# Entry box
entry = Entry(root, width=20, borderwidth=5, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

# Functions
def click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def clear():
    entry.delete(0, END)

def set_operator(op):
    global num1, operator
    num1 = float(entry.get())
    operator = op
    entry.delete(0, END)

def calculate():
    global num1, operator
    try:
        num2 = float(entry.get())

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                entry.delete(0, END)
                entry.insert(0, "Error")
                return
            result = num1 / num2
        else:
            result = 0

        entry.delete(0, END)
        entry.insert(0, result)

    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Buttons
Button(root, text="1", command=lambda: click(1)).grid(row=1, column=0)
Button(root, text="2", command=lambda: click(2)).grid(row=1, column=1)
Button(root, text="3", command=lambda: click(3)).grid(row=1, column=2)

Button(root, text="4", command=lambda: click(4)).grid(row=2, column=0)
Button(root, text="5", command=lambda: click(5)).grid(row=2, column=1)
Button(root, text="6", command=lambda: click(6)).grid(row=2, column=2)

Button(root, text="7", command=lambda: click(7)).grid(row=3, column=0)
Button(root, text="8", command=lambda: click(8)).grid(row=3, column=1)
Button(root, text="9", command=lambda: click(9)).grid(row=3, column=2)

Button(root, text="0", command=lambda: click(0)).grid(row=4, column=1)

# Operators
Button(root, text="+", command=lambda: set_operator("+")).grid(row=1, column=3)
Button(root, text="-", command=lambda: set_operator("-")).grid(row=2, column=3)
Button(root, text="*", command=lambda: set_operator("*")).grid(row=3, column=3)
Button(root, text="/", command=lambda: set_operator("/")).grid(row=4, column=3)

# Equal and Clear
Button(root, text="=", command=calculate).grid(row=4, column=2)
Button(root, text="C", command=clear).grid(row=4, column=0)

# Run app
root.mainloop()