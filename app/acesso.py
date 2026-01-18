import pyodbc
from database import conectar

# Funções de acesso ao banco de dados

# Executar instruções no banco de dados
def executar(sql, params=None):
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(sql, params or [])
            conexao.commit()
            return cursor.rowcount

    except pyodbc.IntegrityError as e:
        raise RuntimeError(f"Violação de integridade: {e}")

    except pyodbc.DatabaseError as e:
        raise RuntimeError(f"Erro ao executar comando no banco: {e}")

    except Exception as e:
        raise RuntimeError(f"Erro inesperado ao executar comando: {e}")

# Realizar consultas no banco de dados
def consultar(sql, params=None):
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(sql, params or [])
            return cursor.fetchall()
        
    except pyodbc.ProgrammingError as e:
        raise RuntimeError(f"Erro de SQL (consulta inválida): {e}")

    except pyodbc.DatabaseError as e:
        raise RuntimeError(f"Erro no banco de dados: {e}")

    except Exception as e:
        raise RuntimeError(f"Erro inesperado na consulta: {e}")
