import tkinter as tk 
from tkinter import * 
from tkinter import ttk 

#Create window 
root = Tk() 
root.title('Fila On-Line Server v0.1') 
root.iconbitmap('D:/Coding/git/fila_online_v0.1/images/fila_online.ico') 
root.geometry("360x233") 
root.resizable(0,0) 

sty = ttk.Style() 
sty.theme_use('clam') 

#Read logfile 
log_file = open('D:/Coding/git/fila_online_v0.1/logs/log_file', 'r')
log_file_array = log_file.read().split(',') 

#Define tree 
tree = ttk.Treeview(root, show = 'headings') 

#Define columns 
tree['columns'] = ("Analista", "Atividade", "Status") 

#Format columns 
tree.column("#0", width = 0) 
tree.column("Analista", anchor = CENTER, width = 120) 
tree.column("Atividade", anchor = CENTER, width = 140) 
tree.column("Status", anchor = CENTER, width = 90) 

#Create headings 
tree.heading("Analista", text = "Analista", anchor = CENTER) 
tree.heading("Atividade", text = "Atividade", anchor = CENTER) 
tree.heading("Status", text = "Status", anchor = CENTER) 

#Fill treeview 
tree.insert('','end', text = "1", values = (log_file_array)) 
 

tree.pack()
root.mainloop()