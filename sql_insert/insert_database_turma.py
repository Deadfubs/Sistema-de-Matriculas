import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('../sistema_de_matriculas.db')

# Cria um cursor
cursor = conn.cursor()

# Insere os dados na tabela
turmas = [
    (101, '08:00-10:00'),
    (102, '10:00-12:00'),
    (201, '13:00-15:00'),
    (202, '15:00-17:00'),
    (301, '17:00-19:00'),
]

cursor.executemany("""
    INSERT INTO turma (sala, horario) 
    VALUES (?, ?)
""", turmas)

# Faz o commit da transação
conn.commit()

# Fecha a conexão
conn.close()
