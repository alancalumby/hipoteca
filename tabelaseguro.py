class TabelaSeguro:

    def __init__(self, percentual_nivel_1, percentual_nivel_2, percentual_nivel_3, percentual_nivel_4, aliquota_nivel_1, aliquota_nivel_2, aliquota_nivel_3, aliquota_nivel_4):
        self.percentual_nivel_1 = percentual_nivel_1
        self.percentual_nivel_2 = percentual_nivel_2    
        self.percentual_nivel_3 = percentual_nivel_3    
        self.percentual_nivel_4 = percentual_nivel_4
        self.aliquota_nivel_1 = aliquota_nivel_1
        self.aliquota_nivel_2 = aliquota_nivel_2
        self.aliquota_nivel_3 = aliquota_nivel_3
        self.aliquota_nivel_4 = aliquota_nivel_4    

    
    def calcular_percentual_seguro(self,percentual_entrada):
        if (percentual_entrada < self.percentual_nivel_1):
            return self.aliquota_nivel_1
        elif (percentual_entrada < self.percentual_nivel_2):
            return self.aliquota_nivel_2
        elif (percentual_entrada < self.percentual_nivel_3):
            return self.aliquota_nivel_3
        else:
            return self.aliquota_nivel_4    