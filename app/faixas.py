from app.acesso import consultar

def listar_todas_as_faixas():
    return consultar("""
        SELECT f.album, f.num_faixa, f.num_disc, f.descricao,
            f.tipo_gravacao, f.tipo_composicao, 
            ISNULL(pm.descricao, 'Não possui') AS periodo
        FROM Faixa f
            LEFT JOIN Compoe c
                ON f.album = c.album
                AND f.num_faixa = c.num_faixa
                AND f.num_disc = c.num_disc
            LEFT JOIN Compositor co
                ON c.compositor = co.codigo
            LEFT JOIN PeriodoMusical pm
                ON co.periodo_musical = pm.codigo
        ORDER BY f.descricao
    """)