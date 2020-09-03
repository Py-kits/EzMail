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

#def Refresh_tab()



EzWindow = tk.Tk()
EzWindow.geometry('600x500')
EzWindow.title("EzMail")

button = tk.Button (
	text="Refresh emails",
	width=20,
	height=5,
	fg="White",	
	bg="blue"
)

mail_buttons = tk.Frame(EzWindow)


btn_Inbox = tk.Button (mail_buttons, text="Inbox")
btn_Spam = tk.Button (mail_buttons, text="Spam")
btn_Important = tk.Button (mail_buttons, text="Important")
btn_Trash = tk.Button (mail_buttons, text="Trash")
btn_Refresh = tk.Button (mail_buttons, text="Refresh")


EzWindow.mainloop()