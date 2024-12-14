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
    copy_status.config(text="Copied to clipboard!")

root = tk.Tk()
root.title("Color Picker")

pick_button = tk.Button(root, text="Pick a Color", command=pick_color)
pick_button.pack(pady=20)

result_label = tk.Label(root, text="RGBA: None")
result_label.pack(pady=20)

copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=10)

copy_status = tk.Label(root, text="")
copy_status.pack(pady=10)

root.mainloop()
