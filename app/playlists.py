from app.acesso import executar, consultar
from datetime import datetime

def criar_playlist(nome):
    try:
        codigo = consultar(
            "SELECT ISNULL(MAX(codigo), 0) + 1 FROM Playlist"
        )[0][0]

        executar("""
            INSERT INTO Playlist (codigo, nome, data_de_criacao, tempo)
            VALUES (?, ?, ?, ?)
        """, (codigo, nome, datetime.now(), 0))

        print(f"Playlist criada com código {codigo}")
        return codigo
    
    except RuntimeError as e:
        raise RuntimeError(f"Erro ao criar playlist: {e}")

def adicionar_faixa_playlist(album, num_faixa, num_disc, playlist):
    executar("""
        INSERT INTO PlaylistFaixa (
            ultima_vez_tocada,
            quantidade_tocada,
            album,
            num_faixa,
            num_disc,
            playlist
        )
        VALUES (GETDATE(), 0, ?, ?, ?, ?)
    """, (album, num_faixa, num_disc, playlist))

def listar_playlists():
    return consultar("""
        SELECT codigo, nome, data_de_criacao 
        FROM Playlist
        ORDER BY nome
    """)

def listar_faixas_de_playlist(playlist):
    return consultar("""
        SELECT f.album, f.num_faixa, f.num_disc, f.descricao,
        f.tipo_gravacao, f.tipo_composicao, ISNULL(pm.descricao, 'Não possui') AS periodo
        FROM Faixa f
            INNER JOIN PlaylistFaixa pf
                on f.album = pf.album
                and f.num_disc = pf.num_disc
                and f.num_faixa = pf.num_faixa
            LEFT JOIN Compoe c
                ON f.album = c.album
                AND f.num_faixa = c.num_faixa
                AND f.num_disc = c.num_disc
            LEFT JOIN Compositor co
                ON c.compositor = co.codigo
            LEFT JOIN PeriodoMusical pm
                ON co.periodo_musical = pm.codigo
            WHERE pf.playlist = ?
            ORDER BY f.descricao
    """, (playlist))

def remover_playlist(playlist):
    return executar("""
        DELETE FROM Playlist
        WHERE codigo = ?
    """, (playlist))

def remover_faixa_da_playlist(playlist, album, num_faixa, num_disc):
    return executar("""
        DELETE FROM PlaylistFaixa
        WHERE playlist = ? 
            AND album = ?
            AND num_faixa = ?
            AND num_disc = ?
    """, (playlist, album, num_faixa, num_disc))

def quantidade_de_albuns_das_playlists():
    return consultar("""
        SELECT * FROM vw_AlbunsDaPlaylist
    """)