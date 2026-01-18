from datetime import datetime
from decimal import Decimal

# Funções para exibir os resultados de maneira formatada

def print_resultados(rows):
    for row in rows:
        valores_formatados = []

        for valor in row:
            if isinstance(valor, datetime):
                valores_formatados.append(
                    valor.strftime("%d/%m/%Y %H:%M:%S")
                )
            elif isinstance(valor, Decimal):
                valores_formatados.append(f"{float(valor):.2f}")
            else:
                valores_formatados.append(str(valor))

        print(" | ".join(valores_formatados))

def print_listar_playlists(rows):
    if not rows:
        print("Nenhuma playlist cadastrada.")
        return

    print("\n======= PLAYLISTS =======")
    for codigo, nome, data in rows:
        data_fmt = data.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Código: {codigo} | Nome: {nome} | Criada em: {data_fmt}")

def print_faixas_playlist(rows):
    if not rows:
        print("Essa playlist não possui faixas.")
        return

    print("\n======= FAIXAS =======")
    for album, num_faixa, num_disc, descricao, tempo, tipo_gravacao, tipo_composicao in rows:
        print(
            f"Álbum: {album} | "
            f"Faixa: {num_faixa} | "
            f"Disco: {num_disc} | "
            f"Nome: {descricao} | "
            f"Tempo: {tempo}seg | "
            f"Gravação: {tipo_gravacao} | "
            f"Composição: {tipo_composicao}"
        )

def print_listar_albuns(rows):
    if not rows:
        print("Nenhum álbum cadastrado.")
        return

    print("\n======= ÁLBUNS =======")
    for codigo, descricao, preco_de_compra, data_gravacao, data_compra, meio_fisico, gravadora in rows:
        print(f"Código: {codigo} | "
              f"Nome: {descricao} | "
              f"Preço: {preco_de_compra} | "
              f"Gravado em: {data_gravacao} | "
              f"Comprado em: {data_compra} | "
              f"Meio fís.: {meio_fisico} | "
              f"Grav.: {gravadora}"
            )

def print_faixas_album(rows):
    if not rows:
        print("Esse álbum não possui faixas.")
        return

    print("\n======= FAIXAS DO ÁLBUM =======")
    for num_faixa, num_disc, descricao, tempo, tipo_gravacao, tipo_composicao in rows:
        print(
            f"Número da faixa: {num_faixa} | "
            f"Número do disco: {num_disc} | "
            f"Nome: {descricao} | "
            f"Tempo: {tempo}seg | "
            f"Gravação: {tipo_gravacao} | "
            f"Composição: {tipo_composicao}"
        )

def print_albuns_acima_da_media(rows):
    if not rows:
        print("Nenhum álbum acima da média.")
        return

    print("\n======= ÁLBUNS ACIMA DA MÉDIA =======")
    for codigo, descricao, preco in rows:
        print(
            f"Código: {codigo} | "
            f"{descricao} | "
            f"Preço: R$ {float(preco):.2f}"
        )

def print_quantidade_albuns_playlists(rows):
    if not rows:
        print("Nenhuma playlist encontrada.")
        return

    print("\n======= ÁLBUNS POR PLAYLIST =======")
    for codigo, nome, quantidade in rows:
        print(
            f"Playlist: {nome} | "
            f"Quantidade de álbuns: {quantidade}"
        )
