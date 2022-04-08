class Hipoteca:

    def __init__(self, valor_casa, valor_entrada, tabelaSeguro, tvq):
        self.valor_casa = valor_casa
        self.valor_entrada = valor_entrada
        self.tabelaSeguro = tabelaSeguro
        self.tvq = tvq
        
        self.validar_config()     

    def validar_config(self):
        if (self.valor_entrada > self.valor_casa):
            print('valor da entrada eh maior do que o valor da casa')
        elif (self.valor_entrada / self.valor_casa < 0.05):
            print('percentual de entrada eh inferior a 5%')

    def calcular_percentual_entrada(self):
        return (self.valor_entrada / self.valor_casa) * 100
    
    def calcular_valor_financiado(self):
        return (self.valor_casa - self.valor_entrada) + (self.valor_casa * self.tabelaSeguro.calcular_percentual_seguro(self.percentual_entrada()) / 100)

    def calcular_percentual_seguro(self):
        return self.tabelaSeguro.calcular_percentual_seguro(self.percentual_entrada())

    def calcular_valor_seguro(self):
        return self.tabelaSeguro.calcular_percentual_seguro(self.calcular_percentual_seguro()) / 100  * self.valor_casa