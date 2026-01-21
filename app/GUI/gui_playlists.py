import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import simpledialog, messagebox

from app.playlists import (
    criar_playlist,
    remover_playlist,
    listar_playlists,
    adicionar_faixa_playlist,
    remover_faixa_da_playlist,
    listar_faixas_de_playlist,
    quantidade_de_albuns_das_playlists,
)

from app.GUI.formatacao import formatar_tabela


def criar_playlists(notebook):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text="Playlists")

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

    def acao_listar():
        mostrar(
            ["Código", "Nome", "Data de criação"],
            listar_playlists()
        )

    def acao_criar():
        nome = simpledialog.askstring("Criar playlist", "Nome da playlist:")
        if nome:
            criar_playlist(nome)
            acao_listar()

    def acao_remover():
        cod = simpledialog.askinteger("Remover playlist", "Código da playlist:")
        if cod is not None:
            remover_playlist(cod)
            acao_listar()

    def acao_adicionar_faixa():
        album = simpledialog.askinteger(
            "Adicionar faixa",
            "Código do álbum:",
            parent=frame
        )
        if album is None:
            return

        num_faixa = simpledialog.askinteger(
            "Adicionar faixa",
            "Número da faixa:",
            parent=frame
        )
        if num_faixa is None:
            return

        num_disc = simpledialog.askinteger(
            "Adicionar faixa",
            "Número do disco:",
            parent=frame
        )
        if num_disc is None:
            return

        playlist = simpledialog.askinteger(
            "Adicionar faixa",
            "Código da playlist:",
            parent=frame
        )
        if playlist is None:
            return

        adicionar_faixa_playlist(album, num_faixa, num_disc, playlist)

        messagebox.showinfo(
            "Sucesso",
            "Faixa adicionada à playlist!",
            parent=frame
        )

        acao_listar()

    def acao_remover_faixa():
        p = simpledialog.askinteger(
            "Remover faixa",
            "Código da playlist:",
            parent=frame
        )
        if p is None:
            return

        album = simpledialog.askinteger(
            "Remover faixa",
            "Código do álbum:",
            parent=frame
        )
        if album is None:
            return

        num_faixa = simpledialog.askinteger(
            "Remover faixa",
            "Número da faixa:",
            parent=frame
        )
        if num_faixa is None:
            return

        num_disc = simpledialog.askinteger(
            "Remover faixa",
            "Número do disco:",
            parent=frame
        )
        if num_disc is None:
            return

        remover_faixa_da_playlist(p, album, num_faixa, num_disc)

        messagebox.showinfo(
            "Sucesso",
            "Faixa removida da playlist!",
            parent=frame
        )

        acao_listar()

    def acao_listar_faixas():
        p = simpledialog.askinteger("Listar faixas", "Código da playlist:")
        if p:
            mostrar(
                ["Álbum", "Nº Faixa", "Nº Disco", "Descrição", "Tipo gravação", "Tipo composição", "Período Musical"],
                listar_faixas_de_playlist(p)
            )

    def acao_qtd_albuns():
        mostrar(
            ["Código", "Playlist", "Qtd Álbuns"],
            quantidade_de_albuns_das_playlists()
        )

    botoes = [
        ("Listar playlists", acao_listar),
        ("Criar playlist", acao_criar),
        ("Remover playlist", acao_remover),
        ("Adicionar faixa", acao_adicionar_faixa),
        ("Remover faixa", acao_remover_faixa),
        ("Faixas da playlist", acao_listar_faixas),
        ("Álbuns por playlist", acao_qtd_albuns),
    ]

    for txt, cmd in botoes:
        ttk.Button(left, text=txt, command=cmd).pack(fill=X, pady=4)

    acao_listar()
