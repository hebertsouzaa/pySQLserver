import pyodbc
from faker import Faker

# Configurar a conexão com o banco de dados SQL Server
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=54.204.79.199;DATABASE=tdm_sefazsp;UID=delphix_db;PWD=delphix_db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Inicializar o objeto Faker com localização em pt_BR
fake = Faker('pt_BR')

# Inserir dados fictícios na tabela Pessoa usando um loop for
for _ in range(600):
    primeiro_nome = fake.first_name()
    segundo_nome = fake.first_name()
    sobrenome = fake.last_name()
    Nome = f"{primeiro_nome} {segundo_nome} {sobrenome}"
    data_nascimento = fake.date_of_birth()

    # Inserir pessoa
    cursor.execute("INSERT INTO Pessoa (Nome, DataNascimento) VALUES (?, ?)", (Nome, data_nascimento))
    conn.commit()  # Comitar para obter o ID da pessoa recém-inserida

    # Recuperar o ID da pessoa recém-inserida
    cursor.execute("SELECT @@IDENTITY AS NewID")
    new_id = cursor.fetchone()[0]

    # Inserir dados fictícios na tabela Documento
    tipo_documento = fake.random_element(elements=('CPF', 'RG', 'Passaporte'))
    numero_documento = fake.unique.random_int(min=10000000, max=99999999)

    cursor.execute("INSERT INTO Documento (TipoDocumento, NumeroDocumento, PessoaID) VALUES (?, ?, ?)",
                   (tipo_documento, numero_documento, new_id))

    # Inserir dados fictícios na tabela Endereco
    logradouro = fake.street_address()
    cidade = fake.city()
    estado = fake.state_abbr()
    
    # Gerar um CEP fictício
    cep = fake.random_int(min=10000000, max=99999999)

    cursor.execute("INSERT INTO Endereco (Logradouro, Cidade, Estado, CEP, PessoaID) VALUES (?, ?, ?, ?, ?)",
                   (logradouro, cidade, estado, cep, new_id))

# Confirmar as operações e fechar a conexão
conn.commit()
conn.close()
