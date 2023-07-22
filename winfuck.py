import tkinter as tk
import random,threading
root = tk.Tk()
root.title('Main Window')
x=200
y=200
def rand(z):
	return random.randint(0,z)
def win():
    top = tk.Toplevel(root)
    top.overrideredirect(1)
    top.geometry(f'{rand(1000)}x{rand(1000)}+{rand(x)*10}+{rand(y)*10}')
    top.config(bg=random.choice(['black','white']))
def open_window():
    for _ in range(400):
        threading.Thread(target=win).start()

button = tk.Button(root, text='Open portal to hell', command=open_window)
button.pack()
root.attributes('-topmost', True)
root.mainloop()