import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.insert("1.0", content)

# Create the main window
window = tk.Tk()
window.title("Text File Reader")

# Create a text area
text_area = tk.Text(window)
text_area.pack()

# Create an "Open" button
open_button = tk.Button(window, text="Open File", command=open_file)
open_button.pack()

# Start the main loop
window.mainloop()
