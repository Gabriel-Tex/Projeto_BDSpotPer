from playlists import *
from consultas import *
from albuns import *
from utils import *

# interface no terminal 

def menu():
    print("\n========= MENU =========")
    print("1 - Criar playlist")
    print("2 - Remover playlist")
    print("3 - Listar playlists")
    print("4 - Adicionar faixa a playlist")
    print("5 - Remover faixa da playlist")
    print("6 - Listar faixas de playlist")
    print("7 - Listar álbuns")
    print("8 - Listar faixas de álbum")
    print("9 - Álbuns acima da média")
    print("10 - Gravadora com mais playlists com faixas de Dvorack")
    print("11 - Compositor com mais faixas nas playlists")
    print("12 - Playlists só com Concerto Barroco")
    print("13 - Quantidade de álbuns de cada playlist")
    print("0 - Sair")

while True:
    try:
        menu()
        op = input("Escolha: ").strip()

        if op == '1':
            nome = input("\nNome da playlist: ").strip()
            criar_playlist(nome)

        elif op == '2':
            playlist = input("\nCódigo da playlist: ")
            rowscount = remover_playlist(playlist)
            if rowscount == 0:
                raise RuntimeError("Playlist não encontrada.")
            else:
                print("\nPlaylist removida com sucesso!")

        elif op == '3':
            rows = listar_playlists()
            print_listar_playlists(rows)

        elif op == '4':
            album = input("\nCódigo do álbum: ")
            num_faixa = input("Número da faixa: ")
            num_disc = input("Número do disco: ")
            playlist = input("Código da playlist: ")
    
            adicionar_faixa_playlist(album, num_faixa, num_disc, playlist)
            print("\nFaixa adicionada com sucesso!")
        
        elif op == '5':
            album = input("\nCódigo do álbum: ")
            num_faixa = input("Número da faixa: ")
            num_disc = input("Número do disco: ")
            playlist = input("Código da playlist: ")

            remover_faixa_da_playlist(playlist, album, num_faixa, num_disc)
            print("\nFaixa removida com sucesso!")

        elif op == '6':
            playlist = input("\nCódigo da playlist: ")
            rows = listar_faixas_de_playlist(playlist)
            print_faixas_playlist(rows)

        elif op == '7':
            rows = listar_albuns()
            print_listar_albuns(rows)

        elif op == '8':
            album = input("\nCódigo do álbum: ")
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

        else:
            print("\nOpção inválida!")
    
    except ValueError:
            print("Entrada inválida. Digite um número válido.")

    except RuntimeError as e:
            print(f"Erro. {e}")

    except Exception as e:
            print("Erro inesperado.", e)