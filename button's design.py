import tkinter as tk
def hello():
    name = entry.get()
    label.config(text=f"Привет, {name}!!")
root = tk.Tk()
root.title("Hello")
label = tk.Label(root, text="Введите Ваше имя", bg="lightgreen")
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Нажми", bg="lightpink", command=hello)
button.pack()
root.mainloop()

