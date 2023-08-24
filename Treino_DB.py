import sqlite3

conn = sqlite3.connect("treino.db")

def criarTabela(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS treino
                (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                cor TEXT NOT NULL )''')

def criarRegistro(conn, nome, idade, cor):
    conn.execute("INSERT INTO treino (nome, idade, cor) values (?, ?, ?)", (nome, idade, cor))
    conn.commit()
    print("Registro incluído com sucesso")

def listaRegistro(conn):
    registros = conn.execute("SELECT * FROM treino").fetchall()
    conn.commit()
    for registro in registros:
        print(registro)
    return registros

def atualizaRegistro(conn, id, **kwargs):
    for parametro, valor in kwargs.items():
        conn.execute("UPDATE treino SET " + parametro + " = ? WHERE ID = ?", (valor, id))
        conn.commit
    print(f"Registro de id {id} atualizado com sucesso")

def excluiRegistro(conn, id):
    conn.execute("DELETE FROM treino WHERE ID = ?", (id,))
    conn.commit()
    print(f"Registro de id {id} excluido com sucesso")

if __name__ == '__main__':
    criarTabela(conn)

    criarRegistro(conn, 'Adelaide', 10, 'Tigrada')
    criarRegistro(conn, 'Celeste', 5, 'Tigrada e Branca')
    criarRegistro(conn, 'Tartaruga', 2, 'Escama')
    criarRegistro(conn, 'Frufrinha', 4, 'Malhada')
    criarRegistro(conn, 'Fulano', 100, 'Verde')
    listaRegistro(conn)
    atualizaRegistro(conn, 10, idade = 20, cor = 'Azul')
    listaRegistro(conn)
    excluiRegistro(conn, 15)
    listaRegistro(conn)
    


