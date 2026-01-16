import sys
import os
from datetime import datetime

# Adicionar o diretório 'app' ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from acesso import executar, consultar

print("=== INSERINDO DADOS DE TESTE NO BANCO ===\n")

try:
    # 1. Inserir Período Musical
    print("1. Inserindo Período Musical (Barroco)...")
    try:
        executar("""
            INSERT INTO PeriodoMusical (codigo, descricao, intervaloInicio, intervaloFim)
            VALUES (1, 'Barroco', 1600, 1750)
        """)
        print("   ✓ Período Musical inserido\n")
    except:
        print("   ⚠ Período Musical pode já existir\n")
    
    # 2. Inserir uma Gravadora
    print("2. Inserindo Gravadora...")
    try:
        executar("""
            INSERT INTO Gravadora (codigo, nome, endereco, home_page)
            VALUES (1, 'Sony Music', 'Rua das Flores, 123', 'www.sonymusic.com')
        """)
        print("   ✓ Gravadora inserida\n")
    except:
        print("   ⚠ Gravadora pode já existir\n")
    
    # 3. Inserir um Álbum
    print("3. Inserindo Álbum...")
    try:
        executar("""
            INSERT INTO Album (codigo, descricao, preco_de_compra, data_gravacao, data_compra, meio_fisico, gravadora)
            VALUES (1, 'Álbum Clássico Barroco', 89.90, '2022-01-15', '2023-01-15', 'CD', 1)
        """)
        print("   ✓ Álbum inserido\n")
    except:
        print("   ⚠ Álbum pode já existir\n")
    
    # 4. Inserir Faixa
    print("4. Inserindo Faixa...")
    try:
        executar("""
            INSERT INTO Faixa (album, num_faixa, num_disc, descricao, tempo, tipo_gravacao, tipo_composicao)
            VALUES (1, 1, 1, 'Concerto em Re Maior', 300, 'ADD', 'Concerto')
        """)
        print("   ✓ Faixa inserida\n")
    except:
        print("   ⚠ Faixa pode já existir\n")
    
    # 5. Inserir Compositor
    print("5. Inserindo Compositor...")
    try:
        executar("""
            INSERT INTO Compositor (codigo, nome, data_de_nascimento, periodo_musical)
            VALUES (1, 'Johann Sebastian Bach', '1685-03-21', 1)
        """)
        print("   ✓ Compositor inserido\n")
    except:
        print("   ⚠ Compositor pode já existir\n")
    
    # 6. Inserir relação Compoe
    print("6. Inserindo relação Compoe...")
    try:
        executar("""
            INSERT INTO Compoe (album, num_faixa, num_disc, compositor)
            VALUES (1, 1, 1, 1)
        """)
        print("   ✓ Relação Compoe inserida\n")
    except:
        print("   ⚠ Relação Compoe pode já existir\n")
    
    # 7. Inserir Playlist
    print("7. Inserindo Playlist...")
    try:
        executar("""
            INSERT INTO Playlist (codigo, nome, data_de_criacao, tempo)
            VALUES (1, 'Minha Playlist Teste', ?, 0)
        """, (datetime.now(),))
        print("   ✓ Playlist inserida\n")
    except:
        print("   ⚠ Playlist pode já existir\n")
    
    # 8. Inserir Faixa na Playlist
    print("8. Inserindo Faixa na Playlist...")
    try:
        executar("""
            INSERT INTO PlaylistFaixa (ultima_vez_tocada, quantidade_tocada, album, num_faixa, num_disc, playlist)
            VALUES (?, 0, 1, 1, 1, 1)
        """, (datetime.now(),))
        print("   ✓ Faixa adicionada à playlist\n")
    except:
        print("   ⚠ Faixa na playlist pode já existir\n")
    
    print("=" * 50)
    print("✅ DADOS PROCESSADOS COM SUCESSO!")
    print("=" * 50)
    
    # Verificar dados inseridos
    print("\n=== VERIFICANDO DADOS INSERIDOS ===\n")
    
    playlists = consultar("SELECT codigo, nome FROM Playlist")
    print("Playlists criadas:")
    for pl in playlists:
        print(f"  - ID: {pl[0]}, Nome: {pl[1]}")
    
    print()
    
    albuns = consultar("SELECT codigo, descricao FROM Album")
    print("Álbuns cadastrados:")
    for al in albuns:
        print(f"  - ID: {al[0]}, Descrição: {al[1]}")
    
    print("\n✅ Pronto! Agora você pode testar a interface com:")
    print("   python .\\interface\\interface.py")
    
except Exception as e:
    print(f"❌ ERRO ao inserir dados: {str(e)}")
    import traceback
    traceback.print_exc()
