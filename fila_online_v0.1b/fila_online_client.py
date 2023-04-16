import tkinter as tk
from tkinter import *
from tkinter import ttk
import getpass
import csv

#function to get current user from pc
def get_user_name():
        user = getpass.getuser()
        return user

#function to save log.csv
def save_log(user, status):  
    col = ['Analista', 'Status']
    lin = [[user, status]]
    
    with open('')
    
    pass
    
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #root windows configure
        self.title("Fila Online v0.1b")
        self.iconbitmap('D:/Coding/python_files/Fila_Online/fila_online_v0.1b/images/fila_online.ico')
        self.geometry('400x70')
        self.resizable(0, 0)
        
        #grid configure
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 3)
        
        self.create_widgets()
      
    def create_widgets(self):
        def send_log():
            user = get_user_name()
            status = status_options.get()
            
            save_log(user.upper(), status)
     
        
        #analista name label
        analista_label = ttk.Label(self, text = "Analista: ")
        analista_label.grid(column = 0, 
                            row = 0, 
                            sticky = tk.W, 
                            padx = 5, 
                            pady = 5)
        
        #analista name display
        username = get_user_name()
        analista_name = Text(self, 
                            height = 1,
                            width = 16)
        analista_name.grid(column = 0, 
                           row = 0,
                           sticky= tk.E, 
                           padx = 22, 
                           pady = 5)
        #config
        analista_name.insert('end', username.upper())
        analista_name.config(state = DISABLED)

        #analista status label
        analista_label = ttk.Label(self, text = "Status: ")
        analista_label.grid(column = 0, 
                            row = 1, 
                            sticky = tk.W, 
                            padx = 5, 
                            pady = 5)
        
        #analista status options
        status_options = ttk.Combobox(self) 
        status_options.grid(column = 0,
                            row = 1,
                            sticky= tk.E, 
                            padx = 22, 
                            pady = 5)
        #config
        status_options['values'] = ['DISPONÍVEL', 'BANHEIRO', 'CHAT']
        status_options['state'] = 'readonly'
        status_options.current(0)
        
        #status save button
        save_status = ttk.Button(self, text = "Salvar", command = send_log)
        save_status.grid(column = 1,
                         row = 1,
                         sticky = tk.E)

if __name__ == "__main__":
    app = App()
    app.mainloop()        