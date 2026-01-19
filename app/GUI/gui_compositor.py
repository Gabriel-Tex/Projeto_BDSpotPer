import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import simpledialog

from app.compositor import obrasDoCompositor, listar_compositores
from app.GUI.formatacao import formatar_tabela

def criar_obras_compositor(notebook):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Obras do Compositor")

    left = ttk.Frame(frame, width=260)
    left.pack(side=LEFT, fill=Y, padx=10, pady=10)

    right = ttk.Frame(frame)
    right.pack(side=RIGHT, expand=True, fill=BOTH, padx=10, pady=10)

    output = ttk.Text(
        right,
        font=("Consolas", 11),
        wrap="none"
    )
    output.pack(expand=True, fill=BOTH)

    def mostrar(cab, dados):
        output.delete("1.0", END)
        output.insert(END, formatar_tabela(cab, dados))

    def acao_listar_compositores():
        mostrar(
            ["Código", "Nome", "Cidade natal", "Nascimento", "Falecimento", "Período musical"],
            listar_compositores()
        )

    def acao_obras_compositor():
        nome = simpledialog.askstring(
            "Obras do compositor",
            "Nome do compositor:",
            parent=frame
        )
        if not nome:
            return

        mostrar(
            ["Álbum", "Nome", "Data de gravação", "Preço", "Meio físico"],
            obrasDoCompositor(nome)
        )

    botoes = [
        ("Listar compositores", acao_listar_compositores),
        ("Obras do compositor", acao_obras_compositor),
    ]

    for txt, cmd in botoes:
        ttk.Button(left, text=txt, command=cmd).pack(fill=X, pady=4)

    acao_listar_compositores()
