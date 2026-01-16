from database import get_connection

try:
    with get_connection() as conexao:
        print("Conectado com sucesso!")
except Exception as e:
    print("Erro:", e)
