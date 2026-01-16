import pyodbc

def conectar():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-MV20600\\SQLDEV2022;"
        "DATABASE=BDSpotPer;"
        "Trusted_Connection=yes;"
    )

def executar(sql, params=None):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(sql, params or [])
        conexao.commit()

def consultar(sql, params=None):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(sql, params or [])
        return cursor.fetchall()
