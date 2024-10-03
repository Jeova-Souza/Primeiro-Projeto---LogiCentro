import pymysql


conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='dblogicentro'
)
cursor = conexao.cursor()

# Inserir dados no banco de dados na tabela usuário, dados fornecidos pelo usuario

print("Cadastra usuário no banco de dados, informe os dados a seguir:")
nome = input("Nome: ")
email = input("Email: ")
usuario = input("Digite nome para seu usuário: ")
senha = input("Digite uma senha: ")
cargo = input("Digite o cargo: ")

comando_sql = "INSERT INTO tb_usuario(nome, email, usuario, senha, cargo) VALUES (%s, %s, %s, %s, %s)"
cursor.execute(comando_sql, (nome, email, usuario, senha, cargo)) # Usar executemany para a inserção de varias linhas

conexao.commit()

print(cursor.rowcount,"registro inserido com sucesso!")