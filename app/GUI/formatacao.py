def formatar_tabela(cabecalhos, dados):
    if not dados:
        return "Nenhum resultado encontrado."

    dados = [list(linha) for linha in dados]
    cab = list(cabecalhos)

    num_colunas = max(len(linha) for linha in dados)

    while len(cab) < num_colunas:
        cab.append("")

    for linha in dados:
        while len(linha) < num_colunas:
            linha.append("")

    larguras = []
    for i in range(num_colunas):
        maior = len(str(cab[i]))
        for linha in dados:
            maior = max(maior, len(str(linha[i])))
        larguras.append(maior)

    def formatar_linha(linha):
        return " | ".join(
            str(linha[i]).ljust(larguras[i])
            for i in range(num_colunas)
        )

    separador = "-+-".join("-" * l for l in larguras)

    resultado = [
        formatar_linha(cab),
        separador
    ]

    for linha in dados:
        resultado.append(formatar_linha(linha))

    return "\n".join(resultado)
