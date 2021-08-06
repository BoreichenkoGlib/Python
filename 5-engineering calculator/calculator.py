from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

# створюю вікно і даю йому назву
root = Tk()
root.title("Calculator boreichenko ki4")
# список з іменами кнопок калькулятора
bttn_list = [
    "7", "8", "9", "+", "*",
    "4", "5", "6", "-", "/",
    "1", "2", "3", "=", "xⁿ",
    "0", ".", "±", "C",
    "Exit", "π", "sin", "cos",
    "(", ")", "n!", "√2", ]
# створюю кнопки
r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd, width=10).grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1
# поле вводу
calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)


# логіка калькулятора
def calc(key):
    global memory
    if key == "=":
        # виключення для написання слів
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
        # вичислення
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")

    # очищення поля вводу кнопка С
    elif key == "C":
        calc_entry.delete(0, END)
    # функція зміни - на + (при натискані змінює знак на протилежний)
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    # число п
    elif key == "π":
        calc_entry.insert(END, math.pi)
    # функція виходу з програми
    elif key == "Exit":
        root.after(1, root.destroy)
        sys.exit()
    # зведення у степінь
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    # синус і косинус
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
    # скобки
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
    # факторіал
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
    # квадратний корінь
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
    # очищення поля після натискання =
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
            calc_entry.insert(END, key)


# закриття вікна tkinter

root.mainloop()
