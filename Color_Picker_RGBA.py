import tkinter as tk
from tkinter.colorchooser import askcolor
import pyperclip

def pick_color():
    color = askcolor()[0]
    if color:
        red, green, blue = [int(c) for c in color]
        alpha = 255
        rgba = f"{{ {red}, {green}, {blue}, {alpha} }}"
        result_label.config(text=f"RGBA: {rgba}")
    else:
        result_label.config(text="No color selected")

def copy_to_clipboard():
    rgba_value = result_label.cget("text").replace("RGBA: ", "")
    pyperclip.copy(rgba_value)
    copy_status.config(text="Copied to clipboard!", fg="green")

root = tk.Tk()
root.title("Color Picker RGBA")

# Set window icon
try:
    root.iconbitmap("color-picker.ico")
except tk.TclError:
    print("Icon file 'color-picker.ico' not found. Please ensure it's in the same directory as this script.")

# Set theme colors
background_color = "#282c34"  # Dark background
button_color = "#61afef"  # Blue button
button_hover_color = "#528fb8"  # Hover effect for button
label_color = "#abb2bf"  # Light gray for labels
text_color = "#e5c07b"  # Gold for text

# Configure root window
root.configure(bg=background_color)

# Button hover effect
def on_enter(e):
    e.widget.config(bg=button_hover_color)

def on_leave(e):
    e.widget.config(bg=button_color)

# Pick button
pick_button = tk.Button(
    root, 
    text="Pick a Color", 
    command=pick_color, 
    bg=button_color, 
    fg="white", 
    font=("Arial", 12), 
    relief="raised", 
    bd=2
)
pick_button.bind("<Enter>", on_enter)
pick_button.bind("<Leave>", on_leave)
pick_button.pack(pady=20)

# Result label
result_label = tk.Label(
    root, 
    text="RGBA: None", 
    bg=background_color, 
    fg=text_color, 
    font=("Arial", 12)
)
result_label.pack(pady=20)

# Copy button
copy_button = tk.Button(
    root, 
    text="Copy", 
    command=copy_to_clipboard, 
    bg=button_color, 
    fg="white", 
    font=("Arial", 12), 
    relief="raised", 
    bd=2
)
copy_button.bind("<Enter>", on_enter)
copy_button.bind("<Leave>", on_leave)
copy_button.pack(pady=10)

# Copy status label
copy_status = tk.Label(
    root, 
    text="", 
    bg=background_color, 
    fg="green", 
    font=("Arial", 10)
)
copy_status.pack(pady=10)

root.mainloop()