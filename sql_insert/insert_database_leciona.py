import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('../sistema_de_matriculas.db')

# Cria um cursor
cursor = conn.cursor()

# Insere os dados na tabela
leciona = [
    (1, 1, 1),
    (1, 2, 2),
    (3, 9, 3),
    (4, 12, 4),
]

cursor.executemany("""
    INSERT INTO leciona (professor_id, disciplina_id, turma_id) 
    VALUES (?, ?, ?)
""", leciona)

# Faz o commit da transação
conn.commit()

# Fecha a conexão
conn.close()
