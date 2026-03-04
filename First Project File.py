import tkinter as tk


def change_color():
    background_color = button.cget("bg")

    if background_color == "green":
        button.config(bg="red")
    else:
        button.config(bg="green")


window = tk.Tk()

button = tk.Button(window, text='Sobaan Click Here', command=change_color, bg="green")
button.pack()

window.mainloop()





















