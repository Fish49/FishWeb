'''
gui stuff for FishWeb
-PaiShoFish49
'''
import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

root = ThemedTk("FishWeb Browser", theme="black")
# root.iconbitmap('fishweb.ico')
root.geometry('200x200')

pageArea = ttk.Frame(root)
pageArea.pack()

tabBrowser = ttk.Frame(root)
tabBrowser.pack()

button = ttk.Button(tabBrowser, text='joemama')
button.pack()

root.mainloop()