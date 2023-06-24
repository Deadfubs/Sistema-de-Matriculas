import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('../sistema_de_matriculas.db')

# Cria um cursor
cursor = conn.cursor()

# Insere os dados na tabela
professores = [
    ('Paulo Fernandes', 'paulofernandes@example.com', 'Ciência da Computação', '1970-01-01', 'Rua Principal, 123, apto 101, Centro, São Paulo'),
    ('Rosa Almeida', 'rosaalmeida@example.com', 'Ciência de Dados', '1969-02-02', 'Rua das Acácias, 456, casa 1, Jardim Flores, Rio de Janeiro'),
    ('Adriano Lima', 'adrianolima@example.com', 'Matemática', '1968-03-03', 'Rua do Carvalho, 789, apto 302, Vila Mariana, São Paulo'),
    ('Márcia Oliveira', 'marciaoliveira@example.com', 'Física', '1967-04-04', 'Rua do Pinheiro, 321, Bloco 2, Copacabana, Rio de Janeiro'),
    ('Roberto Castro', 'robertocastro@example.com', 'Química', '1966-05-05', 'Rua do Olmo, 654, apto 405, Moema, São Paulo'),
]

cursor.executemany("""
    INSERT INTO professor (nome, email, curso, data_nascimento, endereco) 
    VALUES (?, ?, ?, ?, ?)
""", professores)

# Faz o commit da transação
conn.commit()

# Fecha a conexão
conn.close()
