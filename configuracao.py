import configparser

class Configuracao:

    ARQUIVO_CFG = 'config.ini'

    def ler_config(self):
        config = configparser.ConfigParser()
        config.read(self.ARQUIVO_CFG)
        return config

    def __init__(self):
        cfg = self.ler_config()
        self.valor_entrada = float(cfg['GERAL']['valor_entrada'])
        self.valor_casa = float(cfg['GERAL']['valor_casa'])
        self.percentual_nivel_1 = float(cfg['TABELA_SEGURO']['percentual_nivel_1'])
        self.percentual_nivel_2 = float(cfg['TABELA_SEGURO']['percentual_nivel_2'])
        self.percentual_nivel_3 = float(cfg['TABELA_SEGURO']['percentual_nivel_3'])
        self.percentual_nivel_4 = float(cfg['TABELA_SEGURO']['percentual_nivel_4'])
        self.aliquota_nivel_1 = float(cfg['TABELA_SEGURO']['aliquota_nivel_1'])
        self.aliquota_nivel_2 = float(cfg['TABELA_SEGURO']['aliquota_nivel_2'])
        self.aliquota_nivel_3 = float(cfg['TABELA_SEGURO']['aliquota_nivel_3'])
        self.aliquota_nivel_4 = float(cfg['TABELA_SEGURO']['aliquota_nivel_4'])
        self.percentual_tvq = float(cfg['IMPOSTO']['percentual_tvq'])
