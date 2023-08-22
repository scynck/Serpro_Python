def criar_aluno(conexao, nome, idade):
    novo_aluno = conexao.execute("INSERT INTO aluno (nome, idade) values (?, ?)", (nome, idade))
    conexao.commit()
    print(f"ALuno {nome} cadastrado")
    return novo_aluno

def listar_alunos(conexao):
    valores = conexao.execute("SELECT * FROM aluno").fetchall()
    conexao.commit()
    print(valores)
    for aluno in valores:
        print(aluno)
    return valores

def atualizar_aluno(conexao, id, **kwargs):
    for parametro, valor in kwargs.items():
        aluno_atualizado = conexao.execute("UPDATE aluno SET " + parametro + " = ? WHERE id = ?", (valor, id))
        conexao.commit()
    print(f"Aluno de id {id} atualizado")
    return aluno_atualizado


def deletar_aluno(conexao, id):
    aluno_deletado = conexao.execute("DELETE FROM aluno WHERE id = ?", (id,))
    return aluno_deletado


if __name__ == '__main__':
    import sqlite3
    conexao = sqlite3.connect("aluno.db")
    conexao.execute('''CREATE TABLE IF NOT EXISTS aluno
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INT NOT NULL)''')
    #criar_aluno(conexao, "Bartolomeu", 4)
    #criar_aluno(conexao, "Tartaruga", 5)

    criar_aluno(conexao, "Beltrano", 100)

    atualizar_aluno(conexao, 4, nome="Fulano")
    print(atualizar_aluno(conexao, 4, idade=80))

    deletar_aluno(conexao, 5)
    listar_alunos(conexao)