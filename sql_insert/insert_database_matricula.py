import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('../sistema_de_matriculas.db')

# Cria um cursor
cursor = conn.cursor()


# Cria um mapeamento entre os cursos e as disciplinas relacionadas
mapeamento_curso_disciplina = {
    'Ciência da Computação': [1, 2, 3, 4, 5, 6],
    'Ciência de Dados': [5, 6, 7, 8],
    'Matemática': [7, 8, 9, 10],
    'Física': [9, 10, 11, 12],
    'Química': [13, 14],
    'Biologia': [15, 16],
    'Geografia': [17, 18],
    'História': [19, 20],
    'Inglês': [19, 20],
    'Arte': [19, 20],
    'Música': [19, 20],
    'Drama': [19, 20],
    'Filosofia': [19, 20],
    'Fotografia': [19, 20],
    'Literatura': [19, 20],
    'Psicologia': [15, 16],
    'Sociologia': [19, 20],
    'Arquitetura': [7, 8, 9, 10],
    'Design Gráfico': [7, 8, 9, 10],
    'Jornalismo': [19, 20],
    # Adicione outros cursos e disciplinas conforme necessário
}

# Obtém os dados dos alunos
cursor.execute("SELECT id, curso FROM aluno")
alunos = cursor.fetchall()

# Cria as combinações de aluno e disciplina
combinacoes = []
for aluno_id, curso in alunos:
    for disciplina_id in mapeamento_curso_disciplina[curso]:
        combinacoes.append((aluno_id, disciplina_id))

cursor.executemany("""
    INSERT INTO matricula (aluno_id, disciplina_id) 
    VALUES (?, ?)
""", combinacoes)

# Faz o commit da transação
conn.commit()

# Fecha a conexão
conn.close()
