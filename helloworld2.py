import tkinter as tk

# Create a function for each operation
def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    label_result.config(text="Result: {:.2f}".format(result))

def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    label_result.config(text="Result: {:.2f}".format(result))

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    label_result.config(text="Result: {:.2f}".format(result))

def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if num2 == 0:
        label_result.config(text="Error: Cannot divide by zero")
    else:
        result = num1 / num2
        label_result.config(text="Result: {:.2f}".format(result))

# Create the GUI
root = tk.Tk()
root.title("Calculator")

# Create input fields
entry1 = tk.Entry(root)
entry1.pack(side=tk.LEFT)
entry2 = tk.Entry(root)
entry2.pack(side=tk.LEFT)

# Create buttons for each operation
button_add = tk.Button(root, text="+", command=add)
button_add.pack(side=tk.LEFT)
button_subtract = tk.Button(root, text="-", command=subtract)
button_subtract.pack(side=tk.LEFT)
button_multiply = tk.Button(root, text="*", command=multiply)
button_multiply.pack(side=tk.LEFT)
button_divide = tk.Button(root, text="/", command=divide)
button_divide.pack(side=tk.LEFT)

# Create a label for the result
label_result = tk.Label(root)
label_result.pack()

# Start the GUI
root.mainloop()