import tkinter as tk
from tkinter import ttk

def main():

    zestawienie = {"a": 1, "b": 2, "c": 3}
    zestawienie2 = {"d": 4, "e": 5, "f": 6}

    root = tk.Tk()
    root.title('Energy')
    root.geometry('500x200')

    def add():
        blank.delete(0, tk.END)
        Ans = zestawienie.get(number1.get()) + zestawienie2.get(number2.get())
        blank.insert(0, Ans)

    tk.Label(root, text="Rodzaj źródła ciepła",bd=3).grid(column=0,row=0)
    number1 = tk.StringVar()
    tk.Label(root, text="System przyhotowania ciepłej wody").grid(column=0,row=2)
    number2= tk.StringVar()

    combo1 = ttk.Combobox(root,values=list(zestawienie.keys()),justify="center",textvariable=number1)
    combo1.bind('<<ComboboxSelected>>', lambda event: label_selected.config(text=zestawienie[number1.get()]))
    combo1.grid(column=0,row=1)
    combo1.current(0)

    combo2 = ttk.Combobox(root,values=list(zestawienie2.keys()),justify="center",textvariable=number2)
    combo2.bind('<<ComboboxSelected>>', lambda event: label_selected1.config(text=zestawienie2[number2.get()]))
    combo2.grid(column=0,row=3)
    combo2.current(0)

    label_selected = tk.Label(root, text="Not Selected")
    label_selected.grid(row=0, column=3)

    label_selected1 = tk.Label(root, text="Not Selected")
    label_selected1.grid(row=0, column=4)

    blank = tk.Entry(root)
    ttk.Label(root, text = "The Answer is:").grid(row=4)
    blank.grid(row=4, column=1)
    tk.Button(root, text='Add', command=add).grid(row=4, column=3)

    root.mainloop()

if __name__ == '__main__':
    main()