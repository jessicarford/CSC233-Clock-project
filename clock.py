'''
Jackson Bradley & Jessica Ford
jbradley22@murraystate.edu & jford30@murraystate.edu
Digital Clock
March 28 2025
'''

import tkinter as tk  # Import the tkinter library
from time import strftime  # Import strftime to format the current time

root = tk.Tk() 
root.title("Digital Clock")  # Set the title of the window
root.geometry('200x78')  #Sets the size of the window


def time():
    # Format the current time in hours, minutes, seconds.
    # Took out the AM/PM, since it's 24h.
    time_format = strftime('%H:%M:%S')# Formats time
    lbl.config(text=time_format)  # Updates with the current time
    lbl.after(1000, time)  # Calls function again after 1 second)
# Creates widget that display the time
lbl = tk.Label(root,
            font=('georgia', 45, 'bold'),  # Set font type, size, and style
            background='white',
            foreground='black')  
lbl.grid(row=0, column=0)
time()  

root.mainloop()
