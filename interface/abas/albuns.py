import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Adicionar o diretório 'app' ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'app'))

from albuns import listar_albuns, listar_faixas_do_album


class AbaAlbuns:
    def __init__(self, notebook):
        """Criar aba para consultar álbuns"""
        self.frame = ttk.Frame(notebook)
        notebook.add(self.frame, text="Álbuns")
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configurar componentes da interface"""
        # Frame para listar álbuns
        frame_albuns = ttk.LabelFrame(self.frame, text="Todos os Álbuns", padding="10")
        frame_albuns.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Treeview para álbuns
        colunas = ("Código", "Descrição")
        self.tree_albuns = ttk.Treeview(frame_albuns, columns=colunas, height=15, show="headings")
        
        for col in colunas:
            self.tree_albuns.heading(col, text=col)
            self.tree_albuns.column(col, width=300)
        
        scrollbar = ttk.Scrollbar(frame_albuns, orient=tk.VERTICAL, command=self.tree_albuns.yview)
        self.tree_albuns.configure(yscroll=scrollbar.set)
        
        self.tree_albuns.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Bind para ver faixas do álbum ao clicar
        self.tree_albuns.bind("<Double-1>", self.mostrar_faixas_album)
        
        # Frame de botões
        frame_botoes = ttk.Frame(self.frame)
        frame_botoes.pack(fill=tk.X, padx=10, pady=10)
        
        btn_atualizar = ttk.Button(frame_botoes, text="Atualizar Lista", command=self.atualizar_albuns)
        btn_atualizar.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(frame_botoes, text="(Duplo clique para ver faixas do álbum)").pack(side=tk.LEFT, padx=5)
        
        # Atualizar ao abrir
        self.atualizar_albuns()
    
    def atualizar_albuns(self):
        """Atualizar lista de álbuns"""
        try:
            # Limpar treeview
            for item in self.tree_albuns.get_children():
                self.tree_albuns.delete(item)
            
            # Buscar álbuns do banco
            albuns = listar_albuns()
            for album in albuns:
                self.tree_albuns.insert("", tk.END, values=album)
        except Exception as e:
            print(f"Erro ao atualizar álbuns: {str(e)}")
            # Não mostrar erro ao usuário na inicialização
    
    def mostrar_faixas_album(self, event):
        """Mostrar faixas de um álbum quando clicado"""
        try:
            item = self.tree_albuns.selection()[0]
            valores = self.tree_albuns.item(item, "values")
            codigo_album = valores[0]
            
            # Buscar faixas
            faixas = listar_faixas_do_album(codigo_album)
            
            if not faixas:
                messagebox.showinfo("Faixas", f"Nenhuma faixa encontrada para o álbum {codigo_album}")
                return
            
            # Criar janela para mostrar faixas
            janela = tk.Toplevel(self.frame)
            janela.title(f"Faixas do Álbum {codigo_album}")
            janela.geometry("600x400")
            
            # Treeview para faixas
            colunas = ("Faixa", "Disco", "Descrição")
            tree_faixas = ttk.Treeview(janela, columns=colunas, height=15, show="headings")
            
            for col in colunas:
                tree_faixas.heading(col, text=col)
                tree_faixas.column(col, width=150)
            
            scrollbar = ttk.Scrollbar(janela, orient=tk.VERTICAL, command=tree_faixas.yview)
            tree_faixas.configure(yscroll=scrollbar.set)
            
            tree_faixas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            for faixa in faixas:
                tree_faixas.insert("", tk.END, values=faixa)
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione um álbum primeiro!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar faixas: {str(e)}")
