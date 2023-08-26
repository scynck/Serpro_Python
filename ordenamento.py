import math
class Ordenar():

    
    def bubble(self, entrada, reverse=False):
        for i in range(len(entrada)-1):
            for i in range(len(entrada)-1):
                if (reverse == False):
                    if (entrada[i] > entrada[i+1]):
                        entrada[i], entrada[i+1] = entrada[i+1], entrada[i]
                else:
                    if (entrada[i] < entrada[i+1]):
                        entrada[i], entrada[i+1] = entrada[i+1], entrada[i]
        return entrada
    
    def quick(self, entrada, iniVet, endVet):   
        i = iniVet
        j = endVet       
        pivo = entrada[round((iniVet + endVet)/2)]

        while(i <= j):
            while (entrada[i] < pivo):
                i = i + 1
            while(entrada[j] > pivo):
                j = j - 1
            if (i<=j):
                aux = entrada[i]
                entrada[i] = entrada[j]
                entrada[j] = aux
                i = i + 1
                j = j - 1
        if (iniVet < j):
            self.quick(entrada, iniVet, j)
        if (i < endVet):
            self.quick(entrada, i, endVet)

        return entrada           
    

if __name__ == '__main__':
    vetor = [9, 6, 4, 10, 5, 1, 2]
    vetor1 = vetor.copy()
    print(vetor)
    print(Ordenar().bubble(vetor))
    print(vetor1)    
    print(Ordenar().quick(vetor, 0, (len(vetor1)-1)))