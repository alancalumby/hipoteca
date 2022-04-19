import hipoteca
from configuracao_geral import ConfiguracaoGeral
from cenario import Cenario
import tabelaseguro

cfg = ConfiguracaoGeral('config.ini')
cenario = Cenario('cenario_01.ini')

tabelaSeguro = tabelaseguro.TabelaSeguro(cfg.percentual_nivel_1, cfg.percentual_nivel_2, cfg.percentual_nivel_3, cfg.percentual_nivel_4, cfg.aliquota_nivel_1, cfg.aliquota_nivel_2, cfg.aliquota_nivel_3, cfg.aliquota_nivel_4)
tvq = cenario.percentual_tvq
hipoteca = hipoteca.Hipoteca(cenario.descricao, cenario.valor_casa, cenario.valor_entrada, tabelaSeguro, tvq)

print('----------------------------------------------------------')
print('Valor da casa (A): ' + str(hipoteca.valor_casa))
print('Valor da entrada (B): ' + str(hipoteca.valor_entrada) + ' (' + str(hipoteca.calcular_percentual_entrada()) + ' %)')
print('----------------------------------------------------------')
print('Valor de base de calculo (C = A - B): ' + str(hipoteca.valor_casa - hipoteca.valor_entrada) )
print('Percentual do seguro (D): ' + str(hipoteca.calcular_percentual_seguro()) + '%')
print('Valor do seguro (E = C * D): ' + str(hipoteca.calcular_valor_seguro()))
print('Percentual do imposto TVQ (F): ' + str(tvq) + '%')
print('Valor do imposto TVQ (G = E * F): ' + str(hipoteca.calcular_valor_imposto_tvq()))
print('Valor financiado (H = C + E): ' + str(hipoteca.calcular_valor_financiado()))
print('----------------------------------------------------------')