from arquivo_configuracao import ArquivoConfiguracao

class Cenario(ArquivoConfiguracao):

    def __init__(self, arquivo):        
        self.arquivo = arquivo
        cfg = self.ler_config()
        self.descricao = cfg['GERAL']['descricao']
        self.valor_entrada = float(cfg['GERAL']['valor_entrada'])
        self.valor_casa = float(cfg['GERAL']['valor_casa'])
        self.percentual_tvq = float(cfg['IMPOSTO']['percentual_tvq'])
        self.taxa_juros = float(cfg['GERAL']['taxa_juros'])
