import sqlite3
import unittest
from Treino_DB import criarRegistro, listaRegistro, atualizaRegistro, excluiRegistro

class Teste_Treino(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS treino
                (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                cor TEXT NOT NULL)''')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_cria_registro(self):
        print("Aqui")
        criarRegistro(self.conn, 'Adelaide', 10, 'Tigrada')
        criarRegistro(self.conn, 'Xuxinha', 1, 'Preta')
        self.saida = self.conn.execute("SELECT * FROM treino").fetchall()
        self.esperado = 2
        self.assertEqual(self.esperado, len(self.saida))

if __name__ == '__main__':
    unittest.main()
        

