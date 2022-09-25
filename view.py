import sqlite3 as lite

con = lite.connect('dados2.db')

#inserir dados

def inserir_form(i):
    with con:
        cur = con.cursor()
        query ="INSERT INTO inventario(nome,local,descrição,marca,data_compra,valor_produto,serie,imagem)VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query,i)

#Atualizar

def atualizar_(i):
    with con:
        cur = con.cursor()
        query ="UPDATE inventario SET nome=?,local=?,descrição=?,marca=?,data_compra=?,valor_produto=?,serie=?,imagem=? WHERE id=?"
        cur.execute(query,i)

#Deletar dados
def deletar_(i):
    with con:
        cur = con.cursor()
        query ="DELETE FROM inventario WHERE id=?"
        cur.execute(query,i)

#ver dados
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados

#ver dados individual


def ver_item(id):
    ver_dados_individual=[]
    with con:
        cur = con.cursor()
        query ="SELECT * FROM inventario WHERE id=?"
        cur.execute(query,id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)
    return ver_dados_individual

