import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
 
window = tk.Tk()
window.title('Calculator')
frame = tk.Frame(master=window, bg="black", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30, font=(20))
entry.grid(row=0, column=0, columnspan=3, ipady=10, pady=5)
 
def myclick(number):
    entry.insert(tk.END, number)
    
def backspace():
    entry.delete(entry.index("end") - 1)
 
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        entry.delete(0, tk.END)
        entry.insert(0,"Syntax Error")
 
def clear():
    entry.delete(0, tk.END)
 
button_1 = tk.Button(master=frame, text='1', font=(20), padx=15,pady=5, width=3, command=lambda: myclick(1), bg="#534E4E", fg='white')

button_1.grid(row=1, column=0, pady=2)

button_2 = tk.Button(master=frame, text='2', font=(20), padx=15,pady=5, width=3, command=lambda: myclick(2), bg="#534E4E", fg='white')

button_2.grid(row=1, column=1, pady=2)

button_3 = tk.Button(master=frame, text='3', font=(20), padx=15,pady=5, width=3, command=lambda: myclick(3), bg="#534E4E", fg='white')

button_3.grid(row=1, column=2, pady=2)

button_4 = tk.Button(master=frame, text='4', font=(20), padx=15,pady=5, width=3, command=lambda: myclick(4), bg="#534E4E", fg='white')

button_4.grid(row=2, column=0, pady=2)

button_5 = tk.Button(master=frame, text='5', font=(20), padx=15,pady=5, width=3, command=lambda: myclick(5), bg="#534E4E", fg='white')

button_5.grid(row=2, column=1, pady=2)

button_6 = tk.Button(master=frame, text='6', font=(20), padx=15,pady=5, width=3, command=lambda: myclick(6), bg="#534E4E", fg='white')

button_6.grid(row=2, column=2, pady=2)

button_7 = tk.Button(master=frame, text='7', font=(20), padx=15,pady=5, width=3, command=lambda: myclick(7), bg="#534E4E", fg='white')

button_7.grid(row=3, column=0, pady=2)

button_8 = tk.Button(master=frame, text='8', font=(20), padx=15,pady=5, width=3, command=lambda: myclick(8), bg="#534E4E", fg='white')

button_8.grid(row=3, column=1, pady=2)

button_9 = tk.Button(master=frame, text='9', font=(20), padx=15,pady=5, width=3, command=lambda: myclick(9), bg="#534E4E", fg='white')

button_9.grid(row=3, column=2, pady=2)

button_0 = tk.Button(master=frame, text='0', font=(20), padx=15,pady=5, width=3, command=lambda: myclick(0), bg="#534E4E", fg='white')

button_0.grid(row=4, column=2, pady=2)
 
button_add = tk.Button(master=frame, text="+", font=(20), padx=15,pady=5, width=3, command=lambda: myclick('+'), bg="#534E4E", fg='white')

button_add.grid(row=4, column=0, pady=2)
 
button_subtract = tk.Button(master=frame, text="-", font=(20), padx=15, pady=5, width=3, command=lambda: myclick('-'), bg="#534E4E", fg='white')

button_subtract.grid(row=4, column=1, pady=2)
 
button_multiply = tk.Button(master=frame, text="*", font=(20), padx=15, pady=5, width=3, command=lambda: myclick('*'), bg="#534E4E", fg='white')

button_multiply.grid(row=5, column=0, pady=2)
 
button_div = tk.Button(master=frame, text="/", font=(20), padx=15,pady=5, width=3, command=lambda: myclick('/'), bg="#534E4E", fg='white')

button_div.grid(row=5, column=1, pady=2)
 
button_clear = tk.Button(master=frame, text="AC", font=(20), padx=15, pady=5, width=3, command=clear, bg='red', fg='white')

button_clear.grid(row=6, column=0, pady=2)

button_backspace = tk.Button(master=frame, text="DEL", font=(20),padx=15, pady=5, width=3, command=backspace, bg='red', fg='white')

button_backspace.grid(row=6, column=1, pady=2)
 
button_equal = tk.Button(master=frame, text="=", font=(20), padx=15,pady=28, width=3, command=equal, bg="green", fg='white')

button_equal.grid(row=5, column=2, rowspan=2, pady=2)
 
window.mainloop()
