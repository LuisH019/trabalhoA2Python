class Inputs:
    def __init__(self):
        None
    
    def input(self, textoInput, min, max):
        valor = 0

        while True:
            try:
                valor = float (input(textoInput))
            except ValueError:
                print = ("Erro: Valor Inválido")
            else:
                if valor < min or valor > max:
                    print = ("Erro: Valor Inválido")
                else:
                    break
        
        return valor
