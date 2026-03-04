# Library for GUI
import tkinter as tk

def button_click():
    print('Hi Mazey!')
    label.config(bg='light pink')
    button.config(bg='light orange')

# Window is here Object for Create Window
window = tk.Tk()

# Giving title to the Window
window.title("My First GUI APP with Sir Ali Haider")

# For Setting Hight, Width... It is String... For Multipy Use small x
window.geometry("400x200")

label = tk.Label(window, text="Hello, Tkinter!", bg="Yellow", font=("Arial", 16))
label.pack()

#Adding Button ... For Button Click write the Function Above
button=tk.Button(window, text='Sobaan Click Me', bg="Sky Blue", command=button_click)
button.pack()

label = tk.Label(window, text="Hello, Tkinter!", fg="blue", bg="yellow", padx=10,
pady=5)
label.pack()

button = tk.Button(window, text="Click Me", width=15, command=lambda:
print("Button clicked!"))
button.pack()

label = tk.Label(window, text="Initial Text")
label.pack()
current_text = label.cget("text")  # Using cget()
print(f"Current text: {current_text}")
current_bg = label.config()["bg"][-1] # Using config() and dictionary access
print(f"Current background: {current_bg}")


# Main Loop must be at the end
window.mainloop()
































