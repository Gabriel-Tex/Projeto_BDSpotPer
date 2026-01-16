import os
import sys
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

print("=== Teste de Configuração do Banco de Dados ===\n")

# Verificar se o arquivo .env existe
env_path = os.path.join(os.path.dirname(__file__), '.env')
print(f"Procurando arquivo .env em: {env_path}")
print(f"Arquivo .env existe? {os.path.exists(env_path)}\n")

# Verificar variáveis carregadas
db_server = os.getenv('DB_SERVER')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

print("Variáveis carregadas:")
print(f"  DB_SERVER: {db_server}")
print(f"  DB_NAME: {db_name}")
print(f"  DB_USER: {db_user}")
print(f"  DB_PASSWORD: {'*' * len(db_password) if db_password else 'NÃO DEFINIDA'}\n")

# Tentar conectar
print("Tentando conectar ao banco de dados...\n")

try:
    import pyodbc
    
    # Listar drivers disponíveis
    drivers = pyodbc.drivers()
    print("Drivers ODBC disponíveis:")
    for driver in drivers:
        print(f"  - {driver}")
    print()
    
    # Tentar conexão
    conexao_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={db_server};"
        f"DATABASE={db_name};"
        f"UID={db_user};"
        f"PWD={db_password};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )
    
    print("String de conexão:")
    print(conexao_string.replace(db_password, "***").replace(db_user, "***") + "\n")
    
    conexao = pyodbc.connect(conexao_string)
    print("✅ CONEXÃO BEM-SUCEDIDA!")
    conexao.close()
    
except pyodbc.Error as e:
    print(f"❌ ERRO DE CONEXÃO: {e}")
except Exception as e:
    print(f"❌ ERRO GERAL: {e}")
