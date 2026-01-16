import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Adicionar o diretório 'app' ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'app'))

from playlists import criar_playlist, listar_playlists, adicionar_faixa_playlist, listar_faixas_de_playlist


class AbaPlaylists:
    def __init__(self, notebook):
        """Criar aba de gerenciamento de playlists"""
        self.frame = ttk.Frame(notebook)
        notebook.add(self.frame, text="Playlists")
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configurar componentes da interface"""
        # Frame para criar playlist
        frame_criar = ttk.LabelFrame(self.frame, text="Criar Nova Playlist", padding="10")
        frame_criar.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(frame_criar, text="Nome:").grid(row=0, column=0, sticky=tk.W)
        self.entrada_nome_playlist = ttk.Entry(frame_criar, width=40)
        self.entrada_nome_playlist.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        
        btn_criar = ttk.Button(frame_criar, text="Criar Playlist", command=self.criar_nova_playlist)
        btn_criar.grid(row=0, column=2, padx=5)
        
        # Frame para listar playlists
        frame_listar = ttk.LabelFrame(self.frame, text="Suas Playlists", padding="10")
        frame_listar.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Treeview para playlists
        colunas = ("Nome", "Data de Criação")
        self.tree_playlists = ttk.Treeview(frame_listar, columns=colunas, height=15, show="headings")
        
        for col in colunas:
            self.tree_playlists.heading(col, text=col)
            self.tree_playlists.column(col, width=300)
        
        scrollbar = ttk.Scrollbar(frame_listar, orient=tk.VERTICAL, command=self.tree_playlists.yview)
        self.tree_playlists.configure(yscroll=scrollbar.set)
        
        self.tree_playlists.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        btn_atualizar = ttk.Button(self.frame, text="Atualizar Lista", command=self.atualizar_playlists)
        btn_atualizar.pack(pady=10)
        
        # Atualizar ao abrir
        self.atualizar_playlists()
    
    def criar_nova_playlist(self):
        """Criar uma nova playlist no banco de dados"""
        nome = self.entrada_nome_playlist.get().strip()
        if not nome:
            messagebox.showwarning("Aviso", "Digite um nome para a playlist!")
            return
        
        try:
            criar_playlist(nome)
            messagebox.showinfo("Sucesso", f"Playlist '{nome}' criada com sucesso!")
            self.entrada_nome_playlist.delete(0, tk.END)
            self.atualizar_playlists()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar playlist: {str(e)}")
    
    def atualizar_playlists(self):
        """Atualizar lista de playlists"""
        try:
            # Limpar treeview
            for item in self.tree_playlists.get_children():
                self.tree_playlists.delete(item)
            
            # Buscar playlists do banco
            playlists = listar_playlists()
            for playlist in playlists:
                self.tree_playlists.insert("", tk.END, values=playlist)
        except Exception as e:
            print(f"Erro ao atualizar playlists: {str(e)}")
            # Não mostrar erro ao usuário na inicialização
