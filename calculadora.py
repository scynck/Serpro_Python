import sqlite3
class CalculadoraAbstrata():

    def __init__(self):
        pass

    def operation(self, op: list) -> str:
        print(op)
        if 'mais' in op: 
            return op[0] + ' mais ' + op[-1] + ' é igual a ' + str(float(op[0]) + float(op[-1]))
        if 'menos' in op: 
            return op[0] + ' menos ' + op[-1] + ' é igual a ' + str(float(op[0]) - float(op[-1]))
        if 'dividido' in op:
            return op[0] + ' dividido por ' + op[-1] + ' é igual a ' + str(float(op[0]) / float(op[-1]))
        if 'vezes' in op: 
            return op[0] + ' vezes ' + op[-1] + ' é igual a ' + str(float(op[0]) * float(op[-1]))
        if 'elevado' in op: 
            return op[0] + ' elevado a ' + op[-1] + ' é igual a ' + str(float(op[0]) ** float(op[-1]))
        else: return 'Informe um comando válido'

    def parser(self, comando: str) -> list:
        comando = comando.lower().strip().split(' ')        
        return comando

    def calcula(self, entrada):
        return self.operation(self.parser(entrada))
    
    
class CalculadoraConsole(CalculadoraAbstrata):
    def __init__(self):
        super().__init__()
    
    def main(self):
        print('''Bem vindo/a à calculadora console! \n
        2 mais 2\n
        2 menos 4\n
        3 vezes 2\n
        6 dividido por 2\n
        4 elevado a 2\n''')    
    
        calculo = input("Escreva o seu cálculo com algum dos formatos acima: ")
        while (calculo == 'Informe um comando válido'):
            calculo = input("Escreva o seu cálculo com algum dos formatos acima: ")
        print(self.calcula(calculo))
        return(self.calcula(calculo))

    def main_test(self, calculo):
        return(self.calcula(calculo))

class CalculadoraArquivo(CalculadoraConsole):
    def __init__(self):
        super().__init__()

    def calcula_e_salva(self, modo):
        resultado = self.main()
        
        with open("output.txt", modo, encoding='utf-8') as f:
            f.write(resultado + "\n")


class CalculadoraDB(CalculadoraConsole):
    conn = sqlite3.connect("simulado1_mock.db")
    def __init__(self):
        super().__init__()

    def createColumn(self):
        
        self.conn.execute("ALTER TABLE calculadora ADD resultado VARCHAR(100)")
        self.conn.commit()

    def calcula_db(self):
        resultado = self.main()
        try:
            c.createColumn()
        except:
            pass
        
        self.conn.execute("INSERT INTO calculadora (entrada, resultados, resultado) values (?,?,?)", ("" , "", resultado))
        self.conn.commit()


if __name__ == '__main__':
    c = CalculadoraDB()    
    c.calcula_db()
    
    
    

        