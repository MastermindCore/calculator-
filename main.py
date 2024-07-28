import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("375x420")
        self.root.config(bg="gray")
        self.root.resizable(False, False)

        self.equation = tk.StringVar()
        self.entry_value = ""
        self.entry = tk.Entry(self.root, width=17, bg="#fff", font=("Arial Bold", 28), textvariable=self.equation)
        self.entry.place(x=0, y=0)

        buttons = [
            {'text': '1', 'x': 0, 'y': 60},
            {'text': '2', 'x': 90, 'y': 60},
            {'text': '3', 'x': 180, 'y': 60},
            {'text': '4', 'x': 0, 'y': 120},
            {'text': '5', 'x': 90, 'y': 120},
            {'text': '6', 'x': 180, 'y': 120},
            {'text': '7', 'x': 0, 'y': 180},
            {'text': '8', 'x': 90, 'y': 180},
            {'text': '9', 'x': 180, 'y': 180},
            {'text': '0', 'x': 90, 'y': 240},
            {'text': '+', 'x': 270, 'y': 60},
            {'text': '-', 'x': 270, 'y': 120},
            {'text': '*', 'x': 270, 'y': 180},
            {'text': '/', 'x': 270, 'y': 240},
            {'text': '=', 'x': 180, 'y': 240},
            {'text': 'C', 'x': 0, 'y': 240}
        ]

        for btn in buttons:
            tk.Button(self.root, width=11, height=4, text=btn['text'], relief='flat', bg='white', command=lambda text=btn['text']: self.show(text)).place(x=btn['x'], y=btn['y'])

    def show(self, value):
        if value == '=':
            self.solve()
        elif value == 'C':
            self.clear()
        else:
            self.entry_value += str(value)
            self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ''

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
