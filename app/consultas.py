from app.acesso import consultar

# Listar os álbuns com preço de compra maior que a média 
# de preços de compra de todos os álbuns.
def albuns_acima_da_media():
    return consultar("""
        SELECT codigo, descricao, preco_de_compra
        FROM Album
        WHERE preco_de_compra >
            (SELECT AVG(preco_de_compra) FROM Album)
    """)

# Listar nome da gravadora com maior número de playlists 
# que possuem pelo uma faixa composta pelo compositor Dvorack
def gravadora_com_mais_playlists_com_faixas_de_dvorack():
    return consultar("""
        SELECT g.nome
        FROM Gravadora g
        INNER JOIN Album a 
            ON g.codigo = a.gravadora
        INNER JOIN Faixa f 
            ON a.codigo = f.album
        INNER JOIN Compoe c 
            ON f.album = c.album
            AND f.num_faixa = c.num_faixa
            AND f.num_disc = c.num_disc
        INNER JOIN Compositor co 
            ON c.compositor = co.codigo
        INNER JOIN PlaylistFaixa pf 
            ON f.album = pf.album
            AND f.num_faixa = pf.num_faixa
            AND f.num_disc = pf.num_disc
        WHERE co.nome = 'Dvorack'
        GROUP BY g.nome
        HAVING COUNT(DISTINCT pf.playlist) = (
            SELECT MAX(qtd_playlist)
            FROM (
                SELECT COUNT(DISTINCT pf2.playlist) as qtd_playlist
                FROM Gravadora g2
                INNER JOIN Album a2 
                    ON g2.codigo = a2.gravadora
                INNER JOIN Faixa f2 
                    ON a2.codigo = f2.album
                INNER JOIN Compoe c2 
                    ON f2.album = c2.album
                    AND f2.num_faixa = c2.num_faixa
                    AND f2.num_disc = c2.num_disc
                INNER JOIN Compositor co2 
                    ON c2.compositor = co2.codigo
                INNER JOIN PlaylistFaixa pf2 
                    ON f2.album = pf2.album
                    AND f2.num_faixa = pf2.num_faixa
                    AND f2.num_disc = pf2.num_disc
                WHERE co2.nome = 'Dvorack'
                GROUP BY g2.nome
            ) qtd
        )
    """)

# Listar nome do compositor com maior número de faixas nas playlists existentes.
def compositor_com_mais_faixas_em_playlists():
    return consultar("""
        SELECT co.nome
        FROM Compositor co
        INNER JOIN Compoe c
            ON co.codigo = c.compositor
        INNER JOIN PlaylistFaixa pf
            ON c.album = pf.album
            AND c.num_faixa = pf.num_faixa
            AND c.num_disc = pf.num_disc
        GROUP BY co.codigo, co.nome 
        HAVING COUNT(*) = (
            SELECT MAX(qtd_faixas)
            FROM (
                SELECT COUNT(*) AS qtd_faixas
                FROM Compositor co2
                INNER JOIN Compoe c2
                    ON co2.codigo = c2.compositor
                INNER JOIN PlaylistFaixa pf2
                    ON c2.album = pf2.album
                    AND c2.num_faixa = pf2.num_faixa
                    AND c2.num_disc = pf2.num_disc
                GROUP BY co2.codigo ) qtd )
    """)

# Listar playlists, cujas faixas (todas) têm tipo de composição "Concerto" e
# período "Barroco".
def playlists_de_composicao_concerto_e_periodo_barroco():
    return consultar("""
        SELECT p.nome
        FROM Playlist p
        WHERE
            EXISTS (
                SELECT * FROM PlaylistFaixa
                WHERE playlist = codigo
            )
            AND NOT EXISTS (
                SELECT * FROM PlaylistFaixa pf
                INNER JOIN Faixa f
                    ON pf.album = f.album
                    AND pf.num_faixa = f.num_faixa
                    AND pf.num_disc = f.num_disc
                LEFT JOIN Compoe c                 
                    ON f.album = c.album
                    AND f.num_faixa = c.num_faixa
                    AND f.num_disc = c.num_disc
                LEFT JOIN Compositor co            
                    ON c.compositor = co.codigo
                LEFT JOIN PeriodoMusical pm        
                    ON co.periodo_musical = pm.codigo
                WHERE pf.playlist = p.codigo
                    AND ( f.tipo_composicao IS NULL OR f.tipo_composicao <> 'Concerto'
                        OR pm.descricao IS NULL OR pm.descricao <> 'Barroco' ) 
            )
    """)
