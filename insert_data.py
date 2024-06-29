import sqlite3

def calcular_gramatura(peso_cheio, peso_vazio):
    return peso_cheio - peso_vazio

def calcular_porcentagem_restante(peso_cheio, peso_retornado):
    return (peso_retornado / peso_cheio) * 100

# Conectar ao banco de dados
conn = sqlite3.connect('cartuchos.db')
cursor = conn.cursor()

# Inserir dados na tabela registro_cartuchos
modelo_cartucho = 'Modelo A'
peso_cheio = 100.0
peso_vazio = 20.0
gramatura = calcular_gramatura(peso_cheio, peso_vazio)
cor = 'Preto'

cursor.execute('''
INSERT INTO registro_cartuchos (modelo_cartucho, peso_cheio, peso_vazio, gramatura, cor)
VALUES (?, ?, ?, ?, ?)
''', (modelo_cartucho, peso_cheio, peso_vazio, gramatura, cor))

# Inserir dados na tabela registro_retornados
cliente_id = 123
filial = 'Filial 1'
peso_retornado = 50.0
porcentagem_restante = calcular_porcentagem_restante(peso_cheio, peso_retornado)

cursor.execute('''
INSERT INTO registro_retornados (modelo_cartucho, peso_cheio, peso_vazio, gramatura, cor, cliente_id, filial, peso_retornado, porcentagem_restante)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (modelo_cartucho, peso_cheio, peso_vazio, gramatura, cor, cliente_id, filial, peso_retornado, porcentagem_restante))

# Confirmar e fechar a conexão
conn.commit()
conn.close()
