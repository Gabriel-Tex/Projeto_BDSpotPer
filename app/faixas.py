from app.acesso import consultar

def listar_todas_as_faixas():
    return consultar("""
        SELECT album, num_faixa, num_disc, descricao, tempo,
             tipo_gravacao, tipo_composicao
        FROM Faixa
    """)