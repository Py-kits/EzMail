import pprint
import ezgmail
import os
import tkinter as tk

app.iconbitmap('path/to/ico/icon.ico')

# Import current mail from 'INBOX'
# Show recent emails in GUI
# Clicking on them shows the entire email and urls

mailapp = tk.Tk()
mailapp.geometry('400x350')
mailapp.title("EzMail")

Refresh_button = tk.Button (
	text="Refresh emails",
	width="20",
	height="5",
	fg="White",	
	bg="blue"
)