import sqlite3 as lite

#conexão
con = lite.connect('dados2.db')
#criação da tabela
with con:
    cur =con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT,local TEXT, descrição TEXT, marca TEXT, data_compra DATE, valor_produto FLOAT, serie TEXT,imagem TEXT)")