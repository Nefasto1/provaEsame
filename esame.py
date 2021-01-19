class ExamException(Exception):
    pass

class Diff:

    def __init__(self, ratio = 1):
        if not isinstance(ratio, int):
            raise ExamException('Tipo ratio non valido')
        if ratio < 1:
            raise ExamException('Valore ratio non valido, solo numeri positivi: {}' .format(lista[i]))

        self.ratio = ratio

    def compute(self, lista):

        if not isinstance(lista, list):
            raise ExamException('Tipo lista non valido')

        lh = len(lista)

        result = []

        for i in range(lh-1):
            if not isinstance(lista[i], (int, float)):
                raise ExamException('Tipo valore non valido: {}' .format(lista[i]))
            if not isinstance(lista[i+1], (int, float)):
                raise ExamException('Tipo valore non valido: {}' .format(lista[i+1]))
                
            dif = lista[i] - lista[i+1]
            if dif < 0:
                dif *= -1;

            result.append(dif/self.ratio)
        
        if len(result) == 0:
            raise ExamException('Impossibile calcolare la differenza, numero elementi non sufficiente')
        
        return result

d = Diff()
d2 = Diff(2)

print(d.compute([1,2]))
print(d2.compute([2,4,8,16]))
