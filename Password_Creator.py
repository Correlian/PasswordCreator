#Import the necessary modules

from tkinter import *
import random
from tkinter import messagebox
from datetime import datetime

# Define the clear fields function

def clear_fields():
    global password_v
    length_entry.delete(0, END)
    repeat_entry.delete(0, END)
    account_entry.delete(0, END)
    password_v.set("")

# Define the password generator function

def generate_password (): #  Declaration of a function to generate a random password in python
    global password_v
    try:  #  Read the user inputs, length and repeat from the entry widgets using get().
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())
        account_name = account_entry.get()
    except: # If the user fails input, code will enter the except block and display an error prompt
        messagebox.showerror(message="Please key in the required inputs")  # Using messagebox.showerror, display the
        return                                                             # error message.

    # Define the character string which contains lowercase, uppercase letters, numbers, and symbols.

    character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[']^_{|}~"

    # This will check if the user allows for repetition of characters

    if repeat == 1: # Use sample for unique characters without repetition
        password = random.sample(character_string, length)
    else:
        password = random.choices(character_string, k=length) # Otherwise, any choices are allowed and it
                                                              # will default to allowing repetition

    # The returned value will be a list, this will be converted to a string using join

    password = ''.join(password)

    # Here we declare a string variable

    password_v = StringVar() # Declare a string variable to substitute the text in the entry widget

    # Assign a variable to 'password' with placeholders "{}" for text which will be inputted by user
    # The 'account_name' and 'password' values will replace the placeholders
    password = "Account: {} - Password: {}".format(account_name, password)

   # Update the content displayed in the GUI to show the generated password with associated account name

    password_v.set(password)

    # Create a read only entry box to view the output, position boxes using place

    password_label = Entry(password_gen, bd=0, bg="gray85", textvariable=password_v, state="readonly")
    password_label.place(x=10, height=50, width=340)

    # This will save password the password to a file called 'passwords.txt' in the same
    # folder as the .py file. Each entry in this will also show the date and time it was created

    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("passwords.txt", "a") as file:
        file.write(f"{password} - {date_time}\n\n")

# Define the user interface, including size and GUI box and the small title

password_gen = Tk()
password_gen.geometry("400x200")
password_gen.title("Password Creator")

# Set background color

password_gen.configure(bg="lightgray")

# Mention the title of this app (including font and size)

title_label = Label(password_gen, text="Tim's Password Generator", font=('Ubuntu Mono', 12))
title_label.pack()

# Read the length of the password (i.e. number of characters)

length_label = Label(password_gen, text="Please enter password length: ")
length_label.place(x=25, y=28)
length_entry = Entry(password_gen, width=3)
length_entry.place(x=190, y=30)

# This will read any repitition and allow the user to chosse if repitition is allowed

repeat_label = Label(password_gen, text="Repetition? 1: no repetition, 2: otherwise: ")
repeat_label.place(x=80, y=58)
repeat_entry = Entry(password_gen, width=3)
repeat_entry.place(x=300, y=60)

# This box will read the user input for the account name linked to the password

account_label = Label(password_gen, text="Account name: ")  # New label for account name
account_label.place(x=20, y=90)  # Position the label
account_entry = Entry(password_gen, width=20)  # Entry field for account name
account_entry.place(x=120, y=90)  # Position the entry field

# Generate the password as per the user input

password_button = Button(password_gen, text="Generate secure password", command=generate_password)
password_button.place(x=110, y=120)

# Add Clear button to the GUI so that the user can start again if they enter incorrect input.

clear_button = Button(password_gen, text="Clear fields", command=clear_fields)
clear_button.place(x=150, y=160)

# Start the GUI main loop

password_gen.mainloop()

# Function to display GitHub account address

def show_github_address():
    messagebox.showinfo("GitHub Account", "My GitHub account is: https://github.com/Correlian")

# Call the function to show the GitHub account address

show_github_address()