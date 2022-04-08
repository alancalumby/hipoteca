import hipoteca
import configuracao
import tabelaseguro

cfg = configuracao.Configuracao()

tabelaSeguro = tabelaseguro.TabelaSeguro(cfg.percentual_nivel_1, cfg.percentual_nivel_2, cfg.percentual_nivel_3, cfg.percentual_nivel_4, cfg.aliquota_nivel_1, cfg.aliquota_nivel_2, cfg.aliquota_nivel_3, cfg.aliquota_nivel_4)
tvq = cfg.percentual_tvq
hipoteca = hipoteca.Hipoteca(cfg.valor_casa, cfg.valor_entrada, tabelaSeguro, tvq)


print('Valor da casa: ' + str(hipoteca.valor_casa))
print('Valor da entrada: ' + str(hipoteca.valor_entrada))
print('Percentual da entrada: ' + str(hipoteca.calcular_percentual_entrada()))
print('Percentual do seguro: ' + str(hipoteca.calcular_percentual_seguro()))
print('Valor do seguro: ' + str(hipoteca.calcular_valor_seguro()))
print('Percentual do imposto TVQ: ' + str(tvq))
print('Valor financiado: ' + str(hipoteca.calcular_valor_financiado()))