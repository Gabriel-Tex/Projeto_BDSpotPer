import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from app.consultas import (
    albuns_acima_da_media,
    gravadora_com_mais_playlists_com_faixas_de_dvorack,
    compositor_com_mais_faixas_em_playlists,
    playlists_de_composicao_concerto_e_periodo_barroco,
)

from app.GUI.formatacao import formatar_tabela

def criar_consultas(notebook):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Consultas")

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

    def mostrar(cabecalho, dados):
        output.delete("1.0", END)
        output.insert(END, formatar_tabela(cabecalho, dados))

    ttk.Button(
        left,
        text="Álbuns acima da média",
        command=lambda: mostrar(
            ["Código", "Descrição", "Preço"],
            albuns_acima_da_media()
        )
    ).pack(fill=X, pady=5)

    ttk.Button(
        left,
        text="Gravadora (Dvorack)",
        command=lambda: mostrar(
            ["Gravadora"],
            gravadora_com_mais_playlists_com_faixas_de_dvorack()
        )
    ).pack(fill=X, pady=5)

    ttk.Button(
        left,
        text="Compositor mais tocado",
        command=lambda: mostrar(
            ["Compositor"],
            compositor_com_mais_faixas_em_playlists()
        )
    ).pack(fill=X, pady=5)

    ttk.Button(
        left,
        text="Playlists Concerto Barroco",
        command=lambda: mostrar(
            ["Playlists"],
            playlists_de_composicao_concerto_e_periodo_barroco()
        )
    ).pack(fill=X, pady=5)
