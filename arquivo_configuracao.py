import configparser

class ArquivoConfiguracao:

    def ler_config(self):
        config = configparser.ConfigParser()
        config.read(self.arquivo)
        return config