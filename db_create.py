import sqlite3

# Conectando ao banco de dados (criará um arquivo chamado "sistema_de_matriculas.db" se não existir)
conn = sqlite3.connect('sistema_de_matriculas.db')

# Criando um cursor
cursor = conn.cursor()

# Criando a tabela "aluno"
cursor.execute('''CREATE TABLE aluno (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    email TEXT,
                    curso TEXT,
                    data_nascimento TEXT,
                    endereco TEXT
                )''')

# Criando a tabela "professor"
cursor.execute('''CREATE TABLE professor (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    email TEXT,
                    curso TEXT,
                    data_nascimento TEXT,
                    endereco TEXT
                )''')

# Criando a tabela "disciplina"
cursor.execute('''CREATE TABLE disciplina (
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    carga_horaria INTEGER
                )''')

# Criando a tabela "turma"
cursor.execute('''CREATE TABLE turma (
                    id INTEGER PRIMARY KEY,
                    sala TEXT,
                    horario TEXT
                )''')

# Criando a tabela "leciona"
cursor.execute('''CREATE TABLE leciona (
                    professor_id INTEGER,
                    disciplina_id INTEGER,
                    turma_id INTEGER,
                    FOREIGN KEY (professor_id) REFERENCES professor (id),
                    FOREIGN KEY (disciplina_id) REFERENCES disciplina (id),
                    FOREIGN KEY (turma_id) REFERENCES turma (id)
                )''')

cursor.execute("""
    CREATE TABLE matricula (
        aluno_id INTEGER,
        disciplina_id INTEGER,
        FOREIGN KEY (aluno_id) REFERENCES aluno (id),
        FOREIGN KEY (disciplina_id) REFERENCES disciplina (id),
        PRIMARY KEY (aluno_id, disciplina_id)
    );
""")

# Salvando as alterações e fechando a conexão
conn.commit()
conn.close()
