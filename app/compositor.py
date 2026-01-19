from app.acesso import consultar

def obrasDoCompositor(nome):
    return consultar("""
        SELECT * FROM fun_ObrasDoCompositor(?)
    """, (nome))

def listar_compositores():
    return consultar("""
        SELECT c.codigo, c.nome, c.cidade_natal, c.data_de_nascimento, 
        data_de_falecimento,pm.descricao
        FROM Compositor c
            INNER JOIN PeriodoMusical pm
                on c.periodo_musical = pm.codigo
    """)