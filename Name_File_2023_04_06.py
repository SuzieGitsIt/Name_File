import tkinter.filedialog as tfd
import tkinter as tk
import os

GUI = tk.Tk()
GUI.title("Op")
GUI.geometry("600x400")
GUI.resizable(False, False)
file_name = ""

def open():
    global file_name
    file_name = tfd.askopenfilename()
    os.startfile(file_name) #open file


btn1 =  tk.Button(GUI, text=f"Open {file_name}", command=open) #button
btn1.place(x = 20, y = 25)

GUI.mainloop()