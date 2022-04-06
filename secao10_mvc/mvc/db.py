import sqlite3
from typing import List


def executar(query: str) -> List[tuple]:
    db_path = './db'
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    resultado = []

    try:
        cursor.execute(query)
        resultado: List[tuple] = cursor.fetchall()
        connection.commit()
    except Exception as e:
        print(f'>>> Erro na execução da query: {e}')
    finally:
        connection.close()

    return resultado
