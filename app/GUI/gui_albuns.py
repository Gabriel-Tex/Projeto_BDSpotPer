import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import simpledialog

from app.albuns import listar_albuns, listar_faixas_do_album
from app.GUI.formatacao import formatar_tabela


def criar_albuns(notebook):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Álbuns")

    left = ttk.Frame(frame, width=250)
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

    def acao_listar_albuns():
        mostrar(
            ["Código", "Descrição", "Preço", "Data compra", "Data lançamento",
            "Meio físico", "Gravadora"],
            listar_albuns()
        )

    def acao_listar_faixas():
        cod = simpledialog.askinteger("Faixas do álbum", "Código do álbum:")
        if cod:
            mostrar(
                ["Álbum", "Nº Faixa", "Nº Disco", "Descrição", "Duração", "Tipo gravação", "Tipo composição"],
                listar_faixas_do_album(cod)
            )

    ttk.Button(
        left,
        text="Listar álbuns",
        command=acao_listar_albuns
    ).pack(fill=X, pady=5)

    ttk.Button(
        left,
        text="Faixas do álbum",
        command=acao_listar_faixas
    ).pack(fill=X, pady=5)

    acao_listar_albuns()
