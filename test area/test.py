import tkinter as tk
root = tk.Tk()
root.title("Test GUI")
label = tk.Label(root, text="Hello creature with eyes.", width=100, height=100, bg="lightblue", fg="red", font=("Arial", 100), borderwidth=2)
label.pack()
button = tk.Button(root, text="Click me", command=lambda: label.config(text="You clicked the button!"))
button.pack()
root.mainloop()