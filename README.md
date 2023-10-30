# pySQLserver
Script para adicionar dados 
CREATE TABLE Pessoa (
        PessoaID INT PRIMARY KEY IDENTITY(1,1),
        Nome VARCHAR(100),
        DataNascimento DATE
    )

	CREATE TABLE Documento (
        DocumentoID INT PRIMARY KEY IDENTITY(1,1),
        TipoDocumento VARCHAR(20),
        NumeroDocumento VARCHAR(20),
        PessoaID INT,
        FOREIGN KEY (PessoaID) REFERENCES Pessoa(PessoaID)
    )

	 CREATE TABLE Endereco (
        EnderecoID INT PRIMARY KEY IDENTITY(1,1),
        Logradouro VARCHAR(100),
        Cidade VARCHAR(50),
        Estado VARCHAR(2),
        CEP VARCHAR(9),
        PessoaID INT,
        FOREIGN KEY (PessoaID) REFERENCES Pessoa(PessoaID)
    )
