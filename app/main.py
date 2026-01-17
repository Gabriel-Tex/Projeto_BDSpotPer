from playlists import (
    criar_playlist,
    listar_playlists,
    adicionar_faixa_playlist,
    listar_faixas_de_playlist,
    remover_playlist,
    remover_faixa_da_playlist,
    quantidade_de_albuns_das_playlists
)
from consultas import (
    albuns_acima_da_media,
    gravadora_com_mais_playlists_com_faixas_de_dvorack,
    compositor_com_mais_faixas_em_playlists,
    playlists_de_composicao_concerto_e_periodo_barroco
)
from albuns import (
    listar_albuns,
    listar_faixas_do_album
)
from utils import (
    print_resultados,
    print_listar_playlists,
    print_faixas_playlist,
    print_listar_albuns,
    print_faixas_album,
    print_albuns_acima_da_media,
    print_quantidade_albuns_playlists
)

while True:
    print("""
1 - Criar playlist
2 - Remover playlist
3 - Listar playlists
4 - Adicionar faixa a playlist
5 - Remover faixa da playlist
6 - Listar faixas de playlist
7 - Listar álbuns
8 - Listar faixas de álbum
9 - Álbuns acima da média
10 - Gravadora com mais playlists com faixas de Dvorack
11 - Compositor com mais faixas nas playlists
12 - Playlists só com Concerto Barroco
13 - Quantidade de álbuns de cada playlist

0 - Sair
""")

    op = input("Escolha: ")
    print('')

    if op == '1':
        nome = input("Nome da playlist: ")
        criar_playlist(nome)

    elif op == '2':
        playlist = input("Código da playlist: ")
        remover_playlist(playlist)
        print("\nPlaylist removida com sucesso!")

    elif op == '3':
        rows = listar_playlists()
        print_listar_playlists(rows)

    elif op == '4':
        album = input("Código do álbum: ")
        num_faixa = input("Número da faixa: ")
        num_disc = input("Número do disco: ")
        playlist = input("Código da playlist: ")
   
        adicionar_faixa_playlist(album, num_faixa, num_disc, playlist)
        print("\nFaixa adicionada com sucesso!")
    
    elif op == '5':
        album = input("Código do álbum: ")
        num_faixa = input("Número da faixa: ")
        num_disc = input("Número do disco: ")
        playlist = input("Código da playlist: ")

        remover_faixa_da_playlist(playlist, album, num_faixa, num_disc)
        print("\nFaixa removida com sucesso!")

    elif op == '6':
        playlist = input("Código da playlist: ")
        rows = listar_faixas_de_playlist(playlist)
        print_faixas_playlist(rows)

    elif op == '7':
        rows = listar_albuns()
        print_listar_albuns(rows)

    elif op == '8':
        album = input("Código do álbum: ")
        rows = listar_faixas_do_album(album)
        print_faixas_album(rows)

    elif op == '9':
        rows = albuns_acima_da_media()
        print_albuns_acima_da_media(rows)

    elif op == '10':
        print("\n======= GRAVADORA =======")
        rows = gravadora_com_mais_playlists_com_faixas_de_dvorack()
        print_resultados(rows)

    elif op == '11':
        print("\n======= COMPOSITOR =======")
        rows = compositor_com_mais_faixas_em_playlists()
        print_resultados(rows)

    elif op == '12':
        print("\n======= PLAYLISTS =======")
        rows = playlists_de_composicao_concerto_e_periodo_barroco()
        print_resultados(rows)
    
    elif op == '13':
        rows = quantidade_de_albuns_das_playlists()
        print_quantidade_albuns_playlists(rows)

    elif op == '0':
        break
