from hipoteca import Hipoteca
from configuracao_geral import ConfiguracaoGeral
from cenarios import Cenarios
import tabelaseguro

cfg = ConfiguracaoGeral('config.ini')
tabelaSeguro = tabelaseguro.TabelaSeguro(cfg.percentual_nivel_1, cfg.percentual_nivel_2, cfg.percentual_nivel_3, cfg.percentual_nivel_4, cfg.aliquota_nivel_1, cfg.aliquota_nivel_2, cfg.aliquota_nivel_3, cfg.aliquota_nivel_4)
cenarios = Cenarios()

for cenario in cenarios.cenarios:
    hipoteca = Hipoteca(cenario.descricao, cenario.valor_casa, cenario.valor_entrada, tabelaSeguro, cenario.percentual_tvq, cenario.taxa_juros)
    hipoteca.relatorio()