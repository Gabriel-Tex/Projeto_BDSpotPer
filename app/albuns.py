from acesso import executar, consultar
from datetime import datetime

def listar_albuns():
    return consultar("""
        SELECT codigo, descricao
        FROM Album
        ORDER BY descricao
    """)

def listar_faixas_do_album(album):
    return consultar("""
        SELECT num_faixa, num_disc, descricao
        FROM Faixa
        WHERE album = ?
        ORDER BY num_disc, num_faixa
    """, (album))