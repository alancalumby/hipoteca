import configparser

ARQUIVO_CFG = 'config.ini'

def ler_config():
    config = configparser.ConfigParser()
    config.read(ARQUIVO_CFG)
    return config

def validar_config(cfg):
    if (float(cfg['GERAL']['entrada']) > float(cfg['GERAL']['valor_casa'])):
        print('valor da entrada eh maior do que o valor da casa')
    elif (float(cfg['GERAL']['entrada']) / float(cfg['GERAL']['valor_casa']) < 0.05):
        print('percentual de entrada eh inferior a 5%')

def percentual_entrada(entrada, valor_casa):
    return (entrada / valor_casa) * 100

def calcular_percentual_seguro(percentual_entrada, cfg):
    if (percentual_entrada < float(cfg['TABELA_SEGURO']['percentual_nivel_1'])):
        return float(cfg['TABELA_SEGURO']['aliquota_nivel_1'])
    elif (percentual_entrada < float(cfg['TABELA_SEGURO']['percentual_nivel_2'])):
        return float(cfg['TABELA_SEGURO']['aliquota_nivel_2'])
    elif (percentual_entrada < float(cfg['TABELA_SEGURO']['percentual_nivel_3'])):
        return float(cfg['TABELA_SEGURO']['aliquota_nivel_3'])
    else:
        return float(cfg['TABELA_SEGURO']['aliquota_nivel_4'])



cfg = ler_config()
percentual_entrada = percentual_entrada(float(cfg['GERAL']['entrada']) , float(cfg['GERAL']['valor_casa']))
validar_config(cfg)
print(str(percentual_entrada))
print(str(calcular_percentual_seguro(percentual_entrada,cfg)))