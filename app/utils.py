from datetime import datetime
from decimal import Decimal

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
