from cenario import Cenario
import os

class Cenarios:

    def __init__(self):
        self.cenarios = self.ler_cenarios()

    def ler_cenarios(self):
        cenarios = []

        import os
        pasta = '.'
        for diretorio, subpastas, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                if arquivo.lower().endswith(".ini") and arquivo.lower().startswith("cenario_"):
                    cenarios.append(Cenario(arquivo))



        #cenario = Cenario('cenario_01.ini')
        #cenarios.append(cenario)
        #cenario = Cenario('cenario_02.ini')
        #cenarios.append(cenario)
        return cenarios