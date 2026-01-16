from playlists import (
    criar_playlist,
    listar_playlists,
    adicionar_faixa_playlist,
    listar_faixas_de_playlist
)
from consultas import (
    albuns_acima_da_media,
    gravadora_mais_playlists_dvorack,
    compositor_mais_faixas_playlists,
    playlists_concerto_barroco
)
from albuns import (
    listar_albuns,
    listar_faixas_do_album
)
from utils import print_resultados

while True:
    print("""
1 - Criar playlist
2 - Remover playlist (imp)
3 - Listar playlists
4 - Adicionar faixa a playlist
5 - Remover faixa da playlist (imp)
6 - Listar faixas de playlist
7 - Listar álbuns
8 - Listar faixas de álbum
9 - Álbuns acima da média
10 - Gravadora com mais playlists com faixas de Dvorack
11 - Compositor com mais faixas nas playlists
12 - Playlists só com Concerto Barroco

0 - Sair
""")

    op = input("Escolha: ")
    print('')

    if op == '1':
        nome = input("Nome da playlist: ")
        criar_playlist(nome)
        print("Playlist criada com sucesso!")

    elif op == '2'
        print("implementar")

    elif op == '3':
        print('======= PLAYLISTS ======')
        rows = listar_playlists()
        print_resultados(rows)

    elif op == '4':
        album = input('Código do álbum: ')
        num_faixa = input('Número da faixa: ')
        num_disc = input('Número do disco: ')
        playlist = input('Código da playlist: ')
   
        adicionar_faixa_playlist(album, num_faixa, num_disc, playlist)
        print("Faixa adicionada com sucesso!")
    
    elif op == '5'
        print('implementar')

    elif op == '6':
        playlist = input('Código da playlist: ')
        print('')
        print('======= FAIXAS ======')
        rows = listar_faixas_de_playlist(playlist)
        print_resultados(rows)

    elif op == '7':
        print('======= ÁLBUNS ======')
        rows = listar_albuns()
        print_resultados(rows)

    elif op == '8':
        album = input('Código do álbum: ')
        print('')
        print('======= FAIXAS ======')
        rows = listar_faixas_do_album(album)
        print_resultados(rows)

    elif op == '9':
        print('======= ÁLBUNS ======')
        rows = albuns_acima_da_media()
        print_resultados(rows)

    elif op == '10':
        print('======= GRAVADORA ======')
        rows = gravadora_mais_playlists_dvorack()
        print_resultados(rows)

     elif op == '11':
        print('======= COMPOSITOR ======')
        rows = compositor_mais_faixas_playlists()
        print_resultados(rows)

    elif op == '12':
        print('======= PLAYLISTS ======')
        rows = playlists_concerto_barroco()
        print_resultados(rows)

    elif op == '0':
        break
