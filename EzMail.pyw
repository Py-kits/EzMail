import pprint
#import ezgmail
import os
import tkinter as tk

#app.iconbitmap('path/to/ico/icon.ico')

# Import current mail from 'INBOX'
# Show recent emails in GUI
# Clicking on them shows the entire email and urls

# Functions for email display

# Functions for email options

#def Inbox_tab()

#def Spam_tab()

#def Importn_tab()

EzWindow = tk.Tk()
EzWindow.geometry('600x500')
EzWindow.title("EzMail")

EzWindow.configure(bg = '#B8E6FF') 


btn_Inbox = tk.Button (
	text="Inbox",
	width=20,
	height=5
)

btn_Spam = tk.Button (
	text="Spam",
	width=20,
	height=5
)


btn_Important = tk.Button (
	text="Important",
	width=20,
	height=5
)

btn_Trash = tk.Button (
	text="Trash",
	width=20,
	height=5
)

btn_Inbox.pack(side="left")
btn_Spam.pack(side="left")
btn_Important.pack(side="left")
btn_Trash.pack(side="left")


EzWindow.mainloop()