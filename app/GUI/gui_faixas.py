import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from app.faixas import listar_todas_as_faixas
from app.GUI.formatacao import formatar_tabela

def criar_faixas(notebook):

    frame = ttk.Frame(notebook, padding=10)
    notebook.add(frame, text="Faixas")

    ttk.Label(
        frame,
        text="Todas as Faixas",
        font=("Segoe UI", 14, "bold")
    ).pack(anchor=W, pady=(0, 10))

    output = ttk.Text(
        frame,
        height=25,
        wrap="none",
        font=("Consolas", 10)
    )
    output.pack(fill=BOTH, expand=True)

    scroll_y = ttk.Scrollbar(frame, orient=VERTICAL, command=output.yview)
    scroll_y.pack(side=RIGHT, fill=Y)
    output.configure(yscrollcommand=scroll_y.set)

    scroll_x = ttk.Scrollbar(frame, orient=HORIZONTAL, command=output.xview)
    scroll_x.pack(side=BOTTOM, fill=X)
    output.configure(xscrollcommand=scroll_x.set)

    def acao_listar():
        output.delete("1.0", END)

        dados = listar_todas_as_faixas()

        cabecalhos = [
            "Álbum", "Nº Faixa", "Nº Disco", "Descrição", "Duração", "Tipo gravação", "Tipo composição"
        ]

        output.insert(END, formatar_tabela(cabecalhos, dados))

    ttk.Button(
        frame,
        text="Listar faixas",
        bootstyle=PRIMARY,
        command=acao_listar
    ).pack(anchor=E, pady=10)

    acao_listar()
