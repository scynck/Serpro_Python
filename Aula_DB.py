import sqlite3

conexao = sqlite3.connect("aula.db")
conexao.execute(''' CREATE TABLE IF NOT EXISTS aluno
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INT NUT NULL);''')
conexao.commit()

def criar_aluno(nome, idade):
    conexao.execute("INSERT INTO aluno (nome, idade) values (?, ?)", (nome, idade))
    conexao.commit()
    print("Aluno inserido com sucesso")

def listar_alunos():
    lista_alunos = conexao.execute("SELECT * FROM aluno")    
    for aluno in lista_alunos:
        print(aluno)

def atualizar_aluno(id, **kwargs):
    for parametro, valor in kwargs.items():
        conexao.execute("UPDATE aluno SET " + parametro + " = ? WHERE id = ?", (valor, id))
        conexao.commit()
    print(f"Aluno de id {id} atualizado com sucesso")
    
def deletar_aluno(id):
    conexao.execute("DELETE FROM aluno WHERE id = ?", (id,))
    conexao.commit()
    print(f"Aluno de id {id} excluido com sucesso")

#criar_aluno("Beltrano", 40)
atualizar_aluno(1, nome="Adelaidezinha", idade=10)
atualizar_aluno(1, idade=20)
deletar_aluno(2)
listar_alunos()
