import tkinter as tk
from time import strftime

# Function to update the time
def time():
    string = strftime('%H:%M:%S %p')  # 24-hour format, time with AM/PM
    label.config(text=string)  # Update the label with the current time
    label.after(1000, time)  # Call the time function again after 1 second (1000 ms)

# Setting up the window
window = tk.Tk()
window.title("Digital Clock")

# Configuring the clock label
label = tk.Label(window, font=('calibri', 50, 'bold'),
                  background='black', foreground='white')
label.pack(anchor='center')

# Start the time function to display the time
time()

# Keep the window open
window.mainloop()
