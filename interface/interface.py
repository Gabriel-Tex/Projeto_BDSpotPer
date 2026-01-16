import tkinter as tk
from tkinter import ttk
import sys
import os

# Adicionar o diretório 'abas' ao path
sys.path.insert(0, os.path.dirname(__file__))

from abas.playlists import AbaPlaylists
from abas.albuns import AbaAlbuns
from abas.consultas import AbaConsultas


class BDSpotPerInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("BDSpotPer - Sistema de Playlists")
        self.root.geometry("1000x700")
        
        # Criar notebook (abas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Criar abas usando classes separadas
        self.aba_playlists = AbaPlaylists(self.notebook)
        self.aba_albuns = AbaAlbuns(self.notebook)
        self.aba_consultas = AbaConsultas(self.notebook)


if __name__ == "__main__":
    root = tk.Tk()
    app = BDSpotPerInterface(root)
    root.mainloop()