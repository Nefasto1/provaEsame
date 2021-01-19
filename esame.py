class ExamException(Exception):
    pass

class Diff:
    
    # Metodo che inizializza l'oggetto
    def __init__(self, ratio = 1):
        # Controllo che la variabile sia un intero positivo
        if not isinstance(ratio, int):
            raise ExamException('Tipo ratio non valido')
        if ratio < 1:
            raise ExamException('Valore ratio non valido, solo numeri positivi: {}' .format(lista[i]))

        self.ratio = ratio

    def compute(self, lista):

        # Controllo che la variabile lista ricevuta da input sia di tipo list
        if not isinstance(lista, list):
            raise ExamException('Tipo lista non valido')

        lh = len(lista)

        result = []

        for i in range(lh-1):

            # Controllo che i valori alle posizioni 'i' ed 'i+1' siano interi o float
            if not isinstance(lista[i], (int, float)):
                raise ExamException('Tipo valore non valido: {}' .format(lista[i]))
            if not isinstance(lista[i+1], (int, float)):
                raise ExamException('Tipo valore non valido: {}' .format(lista[i+1]))
            
            # Eseguo la differenza e, se negativa, la moltiplico per -1 (cambio segno)
            dif = lista[i] - lista[i+1]
            if dif < 0:
                dif *= -1;

            result.append(dif/self.ratio)
        
        # Controllo se non è entrato nel ciclo (i valori non erano sufficienti)
        if len(result) == 0:
            raise ExamException('Impossibile calcolare la differenza, numero elementi non sufficiente')
        
        return result