import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('../sistema_de_matriculas.db')

# Cria um cursor
cursor = conn.cursor()

# Insere os dados na tabela
disciplinas = [
    (1, 'Programação I', 60),
    (2, 'Programação II', 60),
    (3, 'Estruturas de Dados', 90),
    (4, 'Banco de Dados', 90),
    (5, 'Inteligência Artificial', 60),
    (6, 'Análise de Dados', 60),
    (7, 'Estatística', 30),
    (8, 'Probabilidade', 30),
    (9, 'Cálculo I', 90),
    (10, 'Cálculo II', 90),
    (11, 'Física I', 60),
    (12, 'Física II', 60),
    (13, 'Química I', 90),
    (14, 'Química II', 90),
    (15, 'Biologia I', 60),
    (16, 'Biologia II', 60),
    (17, 'Geografia Humana', 60),
    (18, 'Geografia Física', 60),
    (19, 'História do Brasil', 60),
    (20, 'História Mundial', 60),
]

cursor.executemany("""
    INSERT INTO disciplina (id, nome, carga_horaria) 
    VALUES (?, ?, ?)
""", disciplinas)

# Faz o commit da transação
conn.commit()

# Fecha a conexão
conn.close()
