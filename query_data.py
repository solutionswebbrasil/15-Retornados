import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('cartuchos.db')
cursor = conn.cursor()

# Consultar dados da tabela registro_cartuchos
cursor.execute('SELECT * FROM registro_cartuchos')
cartuchos = cursor.fetchall()

print("Registro de Cartuchos:")
for cartucho in cartuchos:
    print(cartucho)

# Consultar dados da tabela registro_retornados
cursor.execute('SELECT * FROM registro_retornados')
retornados = cursor.fetchall()

print("\nRegistro de Retornados:")
for retornado in retornados:
    print(retornado)

# Fechar a conexão
conn.close()
