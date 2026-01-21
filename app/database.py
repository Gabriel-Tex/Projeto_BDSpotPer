import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

# Estabelecer conexão com o banco de dados

def conectar():
    try: 
        conexao = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={os.getenv('DB_SERVER')};"
            f"DATABASE={os.getenv('DB_NAME')};"
            f"UID={os.getenv('DB_USER')};"
            f"PWD={os.getenv('DB_PASSWORD')};"
            "Encrypt=yes;"
            "TrustServerCertificate=yes;"
        )
        return pyodbc.connect(conexao)
    
    except Exception as e:
        raise RuntimeError("Erro ao conectar ao banco de dados") from e
