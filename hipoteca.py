class Hipoteca:

    def __init__(self, descricao, valor_casa, valor_entrada, tabelaSeguro, tvq):
        self.descricao = descricao
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

        if (self.tvq > 100.0 or self.tvq < 0.0):
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

    def relatorio(self):
        print('##########################################################')
        print(self.descricao)
        print('##########################################################')
        print('Valor da casa (A): ' + str(self.valor_casa))
        print('Valor da entrada (B): ' + str(self.valor_entrada) + ' (' + str(self.calcular_percentual_entrada()) + ' %)')
        print('----------------------------------------------------------')
        print('Valor de base de calculo (C = A - B): ' + str(self.valor_casa - self.valor_entrada) )
        print('Percentual do seguro (D): ' + str(self.calcular_percentual_seguro()) + '%')
        print('Valor do seguro (E = C * D): ' + str(self.calcular_valor_seguro()))
        print('Percentual do imposto TVQ (F): ' + str(self.tvq) + '%')
        print('Valor do imposto TVQ (G = E * F): ' + str(self.calcular_valor_imposto_tvq()))
        print('Valor financiado (H = C + E): ' + str(self.calcular_valor_financiado()))