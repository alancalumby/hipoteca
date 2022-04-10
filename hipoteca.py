class Hipoteca:

    def __init__(self, valor_casa, valor_entrada, tabelaSeguro, tvq):
        self.valor_casa = valor_casa
        self.valor_entrada = valor_entrada
        self.tabelaSeguro = tabelaSeguro
        self.tvq = tvq        
        self.validar_config()     

    def validar_config(self):
        if (self.valor_entrada > self.valor_casa):
            raise ValueError('valor da entrada eh maior do que o valor da casa')
        elif (self.valor_entrada / self.valor_casa < 0.05):
            raise ValueError('percentual de entrada eh inferior a 5%')
        elif (self.tvq > 100.0 or self.tvq < 0.0):
            raise ValueError('tvq deve ser entre 0 e 100')

    def calcular_percentual_entrada(self):
        return (self.valor_entrada / self.valor_casa) * 100
    
    def calcular_valor_financiado(self):
        return (self.valor_casa - self.valor_entrada) + (self.calcular_valor_seguro())# + (self.calcular_valor_imposto_tvq())

    def calcular_valor_imposto_tvq(self):
        return self.calcular_valor_seguro() * self.tvq / 100

    def calcular_percentual_seguro(self):
        return self.tabelaSeguro.calcular_percentual_seguro(self.calcular_percentual_entrada())

    def calcular_valor_seguro(self):
        return self.calcular_percentual_seguro() / 100  * (self.valor_casa - self.valor_entrada)