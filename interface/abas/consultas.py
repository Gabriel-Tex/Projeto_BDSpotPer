import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
import os

# Adicionar o diretório 'app' ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'app'))

from consultas import (
    albuns_acima_da_media,
    gravadora_mais_playlists_dvorack,
    compositor_mais_faixas_playlists,
    playlists_concerto_barroco
)


class AbaConsultas:
    def __init__(self, notebook):
        """Criar aba para consultas especializadas"""
        self.frame = ttk.Frame(notebook)
        notebook.add(self.frame, text="Consultas")
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configurar componentes da interface"""
        # Frame de botões para consultas
        frame_botoes = ttk.LabelFrame(self.frame, text="Selecione uma Consulta", padding="10")
        frame_botoes.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(frame_botoes, text="Álbuns acima da média", 
                  command=self.consulta_albuns_media).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(frame_botoes, text="Gravadora + Dvorack", 
                  command=self.consulta_gravadora_dvorack).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(frame_botoes, text="Compositor + Faixas", 
                  command=self.consulta_compositor_faixas).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(frame_botoes, text="Playlists Concerto Barroco", 
                  command=self.consulta_concerto_barroco).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Frame para resultados
        frame_resultado = ttk.LabelFrame(self.frame, text="Resultados", padding="10")
        frame_resultado.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.texto_resultado = scrolledtext.ScrolledText(frame_resultado, height=20, width=100)
        self.texto_resultado.pack(fill=tk.BOTH, expand=True)
        
        # Mensagem inicial
        self.texto_resultado.insert(tk.END, "Selecione uma consulta acima para ver os resultados.")
        self.texto_resultado.config(state=tk.DISABLED)
    
    def _limpar_resultado(self):
        """Limpar área de resultado"""
        self.texto_resultado.config(state=tk.NORMAL)
        self.texto_resultado.delete(1.0, tk.END)
    
    def _inserir_resultado(self, texto):
        """Inserir texto no resultado"""
        self.texto_resultado.insert(tk.END, texto)
        self.texto_resultado.config(state=tk.DISABLED)
    
    def consulta_albuns_media(self):
        """Consultar álbuns acima da média"""
        try:
            self._limpar_resultado()
            albuns = albuns_acima_da_media()
            
            if not albuns:
                self._inserir_resultado("Nenhum álbum encontrado.")
                return
            
            resultado = "=== ÁLBUNS ACIMA DA MÉDIA ===\n\n"
            for album in albuns:
                resultado += f"Código: {album[0]}\n"
                resultado += f"Descrição: {album[1]}\n"
                resultado += f"Preço de Compra: R$ {album[2]:.2f}\n"
                resultado += "-" * 70 + "\n\n"
            
            self._inserir_resultado(resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na consulta: {str(e)}")
            self._limpar_resultado()
            self._inserir_resultado(f"Erro: {str(e)}")
    
    def consulta_gravadora_dvorack(self):
        """Consultar gravadora com mais playlists de Dvorack"""
        try:
            self._limpar_resultado()
            resultado_query = gravadora_mais_playlists_dvorack()
            
            if not resultado_query:
                self._inserir_resultado("Nenhuma gravadora encontrada com faixas de Dvorack.")
                return
            
            resultado = "=== GRAVADORA COM MAIS PLAYLISTS DE DVORACK ===\n\n"
            for row in resultado_query:
                resultado += f"Gravadora: {row[0]}\n"
            
            self._inserir_resultado(resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na consulta: {str(e)}")
            self._limpar_resultado()
            self._inserir_resultado(f"Erro: {str(e)}")
    
    def consulta_compositor_faixas(self):
        """Consultar compositor com mais faixas nas playlists"""
        try:
            self._limpar_resultado()
            resultado_query = compositor_mais_faixas_playlists()
            
            if not resultado_query:
                self._inserir_resultado("Nenhum compositor encontrado.")
                return
            
            resultado = "=== COMPOSITOR COM MAIS FAIXAS NAS PLAYLISTS ===\n\n"
            for row in resultado_query:
                resultado += f"Compositor: {row[0]}\n"
            
            self._inserir_resultado(resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na consulta: {str(e)}")
            self._limpar_resultado()
            self._inserir_resultado(f"Erro: {str(e)}")
    
    def consulta_concerto_barroco(self):
        """Consultar playlists só com Concerto Barroco"""
        try:
            self._limpar_resultado()
            resultado_query = playlists_concerto_barroco()
            
            if not resultado_query:
                self._inserir_resultado("Nenhuma playlist encontrada com apenas composições Concerto Barroco.")
                return
            
            resultado = "=== PLAYLISTS SÓ COM CONCERTO BARROCO ===\n\n"
            for row in resultado_query:
                resultado += f"Playlist: {row[0]}\n"
            
            self._inserir_resultado(resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na consulta: {str(e)}")
            self._limpar_resultado()
            self._inserir_resultado(f"Erro: {str(e)}")
