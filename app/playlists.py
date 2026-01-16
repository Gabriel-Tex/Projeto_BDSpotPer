from acesso import executar, consultar
from datetime import datetime
from utils import print_resultados

def criar_playlist(nome):
    # gerar código manualmente
    codigo = consultar(
        "SELECT ISNULL(MAX(codigo), 0) + 1 FROM Playlist"
    )[0][0]

    executar("""
        INSERT INTO Playlist (codigo, nome, data_de_criacao, tempo)
        VALUES (?, ?, ?, ?)
    """, (codigo, nome, datetime.now(), 0))

    print(f"Playlist criada com código {codigo}")
    return codigo

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
        SELECT nome, data_de_criacao 
        FROM Playlist
        ORDER BY nome
    """)

def listar_faixas_de_playlist(playlist):
    return consultar("""
        SELECT f.num_faixa, f.num_disc, f.descricao 
        FROM Faixa f
	    INNER JOIN PlaylistFaixa pf
            on f.album = pf.album
            and f.num_disc = pf.num_disc
            and f.num_faixa = pf.num_faixa
        WHERE pf.playlist = ?
    """, (playlist,))