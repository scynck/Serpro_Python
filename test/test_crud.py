import unittest
import sqlite3
from Aula_DB import criar_aluno, listar_alunos, atualizar_aluno, deletar_aluno

class Teste_Crud(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS aluno
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     nome TEXT NOT NULL,
                     idade INTEGER NOT NULL) ''')
        self.conn.commit()
        
    def tearDown(self):
        self.conn.close()

    def test_criar_aluno(self):
        criar_aluno(self.conn, "Fulano", 30)
        criar_aluno(self.conn, "Beltrano", 20)
        alunos = self.conn.execute("SELECT * FROM aluno").fetchall()
        self.assertEqual(2, len(alunos))
        self.assertEqual("Beltrano", alunos[1][1])

    def test_listar_aluno(self):
        criar_aluno(self.conn, "Jabiraca", 50)
        criar_aluno(self.conn, "Jabucreia", 30)
        alunos = listar_alunos(self.conn)
        self.assertEqual(2, len(alunos))

    def test_atualizar_aluno(self):
        criar_aluno(self.conn, "Fulano", 30)
        atualizar_aluno(self.conn, 1, nome="Beltrano", idade=20)
        aluno = self.conn.execute("SELECT * FROM aluno WHERE id = 1").fetchone()
        self.assertEqual("Beltrano", aluno[1])
        self.assertNotEqual("Fulano", aluno[1])

    def test_deletar_aluno(self):
        criar_aluno(self.conn, "Jabiraca", 50)
        criar_aluno(self.conn, "Jabucreia", 30)
        deletar_aluno(self.conn, 1)
        alunos = self.conn.execute("SELECT * FROM aluno").fetchall()
        self.assertEqual(1, len(alunos))
        self.assertTrue(alunos[0][1] == "Jabucreia")
        self.assertFalse(alunos[0][1] == "Jabiraca")
        