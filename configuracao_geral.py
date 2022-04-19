from arquivo_configuracao import ArquivoConfiguracao

class ConfiguracaoGeral(ArquivoConfiguracao):

    def __init__(self, arquivo):        
        self.arquivo = arquivo
        cfg = self.ler_config()
        self.percentual_nivel_1 = float(cfg['TABELA_SEGURO']['percentual_nivel_1'])
        self.percentual_nivel_2 = float(cfg['TABELA_SEGURO']['percentual_nivel_2'])
        self.percentual_nivel_3 = float(cfg['TABELA_SEGURO']['percentual_nivel_3'])
        self.percentual_nivel_4 = float(cfg['TABELA_SEGURO']['percentual_nivel_4'])
        self.aliquota_nivel_1 = float(cfg['TABELA_SEGURO']['aliquota_nivel_1'])
        self.aliquota_nivel_2 = float(cfg['TABELA_SEGURO']['aliquota_nivel_2'])
        self.aliquota_nivel_3 = float(cfg['TABELA_SEGURO']['aliquota_nivel_3'])
        self.aliquota_nivel_4 = float(cfg['TABELA_SEGURO']['aliquota_nivel_4'])