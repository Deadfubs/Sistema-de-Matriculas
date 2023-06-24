import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('../sistema_de_matriculas.db')

# Cria um cursor
cursor = conn.cursor()

# Insere os dados na tabela
students = [
    ('João Silva', 'joaosilva@example.com', 'Ciência da Computação', '2000-01-01', 'Rua Principal, 123, apto 101, Centro, São Paulo'),
    ('Maria Santos', 'mariasantos@example.com', 'Ciência de Dados', '1999-02-02', 'Rua das Acácias, 456, casa 1, Jardim Flores, Rio de Janeiro'),
    ('Lucas Pereira', 'lucaspereira@example.com', 'Matemática', '1998-03-03', 'Rua do Carvalho, 789, apto 302, Vila Mariana, São Paulo'),
    ('Julia Costa', 'juliacosta@example.com', 'Física', '1997-04-04', 'Rua do Pinheiro, 321, Bloco 2, Copacabana, Rio de Janeiro'),
    ('Pedro Rocha', 'pedrorocha@example.com', 'Química', '1996-05-05', 'Rua do Olmo, 654, apto 405, Moema, São Paulo'),
    ('Ana Ferreira', 'anaferreira@example.com', 'Biologia', '1995-06-06', 'Rua do Bétula, 987, casa 20, Barra da Tijuca, Rio de Janeiro'),
    ('Mateus Lopes', 'mateuslopes@example.com', 'Geografia', '1994-07-07', 'Rua do Castanheiro, 123, apto 201, Ipiranga, São Paulo'),
    ('Laura Ribeiro', 'lauraribeiro@example.com', 'História', '1993-08-08', 'Rua do Cedro, 456, casa 3, Leblon, Rio de Janeiro'),
    ('Bruno Almeida', 'brunoalmeida@example.com', 'Inglês', '1992-09-09', 'Rua do Abeto, 789, apto 303, Brooklin, São Paulo'),
    ('Mariana Gomes', 'marianagomes@example.com', 'Arte', '1991-10-10', 'Rua do Salgueiro, 321, Bloco 4, Ipanema, Rio de Janeiro'),
    ('Rafael Souza', 'rafaelsouza@example.com', 'Música', '1990-11-11', 'Rua do Choupo, 654, apto 406, Butantã, São Paulo'),
    ('Beatriz Teixeira', 'beatrizteixeira@example.com', 'Drama', '1989-12-12', 'Rua do Faia, 987, casa 21, Recreio dos Bandeirantes, Rio de Janeiro'),
    ('Felipe Cardoso', 'felipecardoso@example.com', 'Filosofia', '1988-01-01', 'Rua das Magnólias, 321, casa 2, Tijuca, Rio de Janeiro'),
    ('Isabela Castro', 'isabelacastro@example.com', 'Fotografia', '1987-02-02', 'Rua das Hortências, 654, apto 507, Pinheiros, São Paulo'),
    ('Carlos Menezes', 'carlosmenezes@example.com', 'Literatura', '1986-03-03', 'Rua das Rosas, 789, apto 304, Grajaú, Rio de Janeiro'),
    ('Daniela Oliveira', 'danielaoliveira@example.com', 'Psicologia', '1985-04-04', 'Rua das Tulipas, 123, Bloco 5, Lapa, São Paulo'),
    ('Roberto Lima', 'robertolima@example.com', 'Sociologia', '1984-05-05', 'Rua das Violetas, 456, casa 4, Botafogo, Rio de Janeiro'),
    ('Camila Araujo', 'camilaaraujo@example.com', 'Arquitetura', '1983-06-06', 'Rua das Orquídeas, 789, apto 305, Santana, São Paulo'),
    ('Luciano Rocha', 'lucianorocha@example.com', 'Design Gráfico', '1982-07-07', 'Rua das Margaridas, 321, casa 5, Flamengo, Rio de Janeiro'),
    ('Marta Souza', 'martasouza@example.com', 'Jornalismo', '1981-08-08', 'Rua das Azaleias, 654, Bloco 6, Liberdade, São Paulo'),
    ('Vitor Raposo', 'vitorraposo@example.com', 'Engenharia de Computação', '1999-02-21', 'Rua Joao Antonio Azeredo, 3, Apto 1001, Belvedere, Belo Horizonte'),
    ('Fúlvio Taroni', 'fulviotaroni@example.com', 'Engenharia de Computação', '1998-05-02', 'Rua Grão Mogol, 287, Bloco 6, Savassi, Belo Horizonte'),
    ('Thiago Bahia', 'thiagobahia@example.com', 'Engenharia de Computação', '1997-03-16', 'Rua Bahia, 123, Bloco 6, Floresta, Belo Horizonte'),
]

cursor.executemany("""
    INSERT INTO aluno (nome, email, curso, data_nascimento, endereco) 
    VALUES (?, ?, ?, ?, ?)
""", students)

# Faz o commit da transação
conn.commit()

# Fecha a conexão
conn.close()
