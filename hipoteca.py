class Hipoteca:

    def __init__(self, valor_casa, valor_entrada, tabelaSeguro):
        self.valor_casa = valor_casa
        self.valor_entrada = valor_entrada
        self.tabelaSeguro = tabelaSeguro
        
        self.validar_config()     

    def validar_config(self):
        if (self.valor_entrada > self.valor_casa):
            print('valor da entrada eh maior do que o valor da casa')
        elif (self.valor_entrada / self.valor_casa < 0.05):
            print('percentual de entrada eh inferior a 5%')

    def percentual_entrada(self):
        return (self.valor_entrada / self.valor_casa) * 100
