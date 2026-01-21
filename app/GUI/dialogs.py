from tkinter import messagebox

def confirmar(msg):
    return messagebox.askyesno("Confirmação", msg)

def erro(msg):
    messagebox.showerror("Erro", msg)

def info(msg):
    messagebox.showinfo("Info", msg)
