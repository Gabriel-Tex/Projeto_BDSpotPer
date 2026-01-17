from acesso import consultar

def listar_albuns():
    return consultar("""
        SELECT codigo, descricao, preco_de_compra, data_gravacao, data_compra,
            meio_fisico, gravadora
        FROM Album
        ORDER BY descricao
    """)

def listar_faixas_do_album(album):
    return consultar("""
        SELECT num_faixa, num_disc, descricao, tempo,
            tipo_gravacao, tipo_composicao
        FROM Faixa
        WHERE album = ?
        ORDER BY num_disc, num_faixa
    """, (album))