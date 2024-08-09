import tkinter as tk
from tkinter import messagebox

class CajeroAutomaticoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cajero Automático")

        self.amount = tk.StringVar()
        self.amount.set("0")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Introduzca cantidad que desea retirar", font=("Helvetica", 20))
        self.label.pack()

        self.text_box = tk.Entry(self.root, textvariable=self.amount, font=("Helvetica", 20), justify='center')
        self.text_box.pack()

        self.amount_buttons = [
            (50000, "50K"), (100000, "100K"), (200000, "200K"),
            (300000, "300K"), (500000, "500K"), (1000000, "1M")
        ]

        self.buttons_frame = tk.Frame(self.root)
        for amount, label in self.amount_buttons:
            button = tk.Button(self.buttons_frame, text=label, font=("Helvetica", 15), command=lambda a=amount: self.set_amount(a))
            button.pack(side='left', padx=5, pady=5)
        self.buttons_frame.pack()

        self.numbers_frame = tk.Frame(self.root)
        for num in range(1, 10):
            button = tk.Button(self.numbers_frame, text=str(num), font=("Helvetica", 15), command=lambda n=num: self.insert_number(n))
            button.grid(row=(num-1)//3, column=(num-1)%3, padx=5, pady=5)
        clear_button = tk.Button(self.numbers_frame, text="C", font=("Helvetica", 15), command=self.clear_text_box)
        clear_button.grid(row=3, column=0, padx=5, pady=5)
        zero_button = tk.Button(self.numbers_frame, text="0", font=("Helvetica", 15), command=lambda: self.insert_number(0))
        zero_button.grid(row=3, column=1, padx=5, pady=5)
        ok_button = tk.Button(self.numbers_frame, text="OK", font=("Helvetica", 15), command=self.cajero_automatico)
        ok_button.grid(row=3, column=2, padx=5, pady=5)
        self.numbers_frame.pack()

        # Etiquetas para mostrar la cantidad de billetes
        self.label100 = tk.Label(self.root, text="Billetes de $100,000: 0", font=("Helvetica", 15))
        self.label100.pack()
        self.label50 = tk.Label(self.root, text="Billetes de $50,000: 0", font=("Helvetica", 15))
        self.label50.pack()
        self.label20 = tk.Label(self.root, text="Billetes de $20,000: 0", font=("Helvetica", 15))
        self.label20.pack()
        self.label10 = tk.Label(self.root, text="Billetes de $10,000: 0", font=("Helvetica", 15))
        self.label10.pack()

    def set_amount(self, value):
        self.amount.set(str(value))

    def insert_number(self, number):
        current_amount = self.amount.get()
        self.amount.set(current_amount + str(number))

    def clear_text_box(self):
        self.amount.set("")

    def Cantidad(self, cantidad):
        billetes = [0, 0, 0, 0]
        contadoresBilletes = [1, 1, 1, 1]
        contador = 1

        while cantidad != 0:
            if cantidad - 10000 >= 0 and contadoresBilletes[0] == 1:
                cantidad -= 10000
                billetes[0] += 1

            if cantidad - 20000 >= 0 and contadoresBilletes[1] == 1:
                cantidad -= 20000
                billetes[1] += 1

            if cantidad - 50000 >= 0 and contadoresBilletes[2] == 1:
                cantidad -= 50000
                billetes[2] += 1

            if cantidad - 100000 >= 0 and contadoresBilletes[3] == 1:
                cantidad -= 100000
                billetes[3] += 1

            if contador == 1:
                contador += 1
                contadoresBilletes = [0, 1, 1, 1]
            elif contador == 2:
                contador += 1
                contadoresBilletes = [0, 0, 1, 1]
            elif contador == 3:
                contador += 1
                contadoresBilletes = [0, 0, 0, 1]
            elif contador == 4:
                contador = 1
                contadoresBilletes = [1, 1, 1, 1]

        self.label100.config(text="Billetes de $100,000: " + str(billetes[3]))
        self.label50.config(text="Billetes de $50,000: " + str(billetes[2]))
        self.label20.config(text="Billetes de $20,000: " + str(billetes[1]))
        self.label10.config(text="Billetes de $10,000: " + str(billetes[0]))

    def cajero_automatico(self):
        cantidad = self.amount.get()
        if not cantidad.isdigit() or int(cantidad) > 1000000:
            messagebox.showerror("Error", "Por favor ingrese una cantidad válida.")
            return

        cantidad = int(cantidad)
        if cantidad % 10000 != 0:
            messagebox.showerror("Error", "La cantidad debe ser múltiplo de $10,000.")
        else:
            messagebox.showinfo("Retiro exitoso", f"Retirando ${cantidad}")
            self.Cantidad(cantidad)

root = tk.Tk()
app = CajeroAutomaticoApp(root)
root.mainloop()
