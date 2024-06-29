import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('cartuchos.db')
cursor = conn.cursor()

# Criar a tabela de registro de cartuchos
cursor.execute('''
CREATE TABLE IF NOT EXISTS registro_cartuchos (
    id INTEGER PRIMARY KEY,
    modelo_cartucho TEXT NOT NULL,
    peso_cheio REAL NOT NULL,
    peso_vazio REAL NOT NULL,
    gramatura REAL NOT NULL,
    cor TEXT NOT NULL
)
''')

# Criar a tabela de registro de retornados
cursor.execute('''
CREATE TABLE IF NOT EXISTS registro_retornados (
    id INTEGER PRIMARY KEY,
    modelo_cartucho TEXT NOT NULL,
    peso_cheio REAL NOT NULL,
    peso_vazio REAL NOT NULL,
    gramatura REAL NOT NULL,
    cor TEXT NOT NULL,
    cliente_id INTEGER NOT NULL,
    filial TEXT NOT NULL,
    peso_retornado REAL NOT NULL,
    porcentagem_restante REAL NOT NULL,
    FOREIGN KEY(modelo_cartucho) REFERENCES registro_cartuchos(modelo_cartucho)
)
''')

# Confirmar e fechar a conexão
conn.commit()
conn.close()
