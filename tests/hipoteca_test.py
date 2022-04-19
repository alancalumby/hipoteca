import unittest
import hipoteca
import tabelaseguro

class TestHipoteca(unittest.TestCase):

    def setUp(self):
        
        self.descricao          = 'teste'
        self.taxa_juros_01      = 1.8
        self.taxa_juros_invalida= -2.0
        self.tvq_valida         = 9.0
        self.tvq_invalida_01    = 999.0
        self.tvq_invalida_02    = -9.0
        self.valor_casa         = 400000
        self.valor_entrada_01   = 80000
        self.valor_entrada_02   = 40000
        self.valor_entrada_03   = 30000
        self.valor_entrada_04   = 60000
        self.valor_entrada_invalida_01   = 600000
        self.valor_entrada_invalida_02   = 600
        self.percentual_nivel_1 = 10
        self.percentual_nivel_2 = 15
        self.percentual_nivel_3 = 20
        self.percentual_nivel_4 = 100
        self.aliquota_nivel_1   = 4.0
        self.aliquota_nivel_2   = 3.1
        self.aliquota_nivel_3   = 2.8
        self.aliquota_nivel_4   = 0
        self.percentual_entrada_1 = 20.0
        self.percentual_entrada_2 = 10.0
        self.percentual_entrada_3 = 7.5
        self.percentual_entrada_4 = 15.0

        self.valor_seguro_1 = self.aliquota_nivel_4 / 100 * (self.valor_casa - self.valor_entrada_01)
        self.valor_seguro_2 = self.aliquota_nivel_2 / 100 * (self.valor_casa - self.valor_entrada_02)
        self.valor_seguro_3 = self.aliquota_nivel_1 / 100 * (self.valor_casa - self.valor_entrada_03)
        self.valor_seguro_4 = self.aliquota_nivel_3 / 100 * (self.valor_casa - self.valor_entrada_04)

        self.valor_imposto_tvq_1 = ((self.valor_casa - self.valor_entrada_01) * self.aliquota_nivel_4 / 100) * self.tvq_valida / 100
        self.valor_imposto_tvq_2 = ((self.valor_casa - self.valor_entrada_02)  * self.aliquota_nivel_2 / 100) * self.tvq_valida / 100
        self.valor_imposto_tvq_3 = ((self.valor_casa - self.valor_entrada_03)  * self.aliquota_nivel_1 / 100) * self.tvq_valida / 100
        self.valor_imposto_tvq_4 = ((self.valor_casa - self.valor_entrada_04)  * self.aliquota_nivel_3 / 100) * self.tvq_valida / 100

        self.valor_financiado_1 = (self.valor_casa - self.valor_entrada_01) + (self.valor_seguro_1)
        self.valor_financiado_2 = (self.valor_casa - self.valor_entrada_02) + (self.valor_seguro_2)
        self.valor_financiado_3 = (self.valor_casa - self.valor_entrada_03) + (self.valor_seguro_3)
        self.valor_financiado_4 = (self.valor_casa - self.valor_entrada_04) + (self.valor_seguro_4)

        self.tabelaSeguro       = tabelaseguro.TabelaSeguro(self.percentual_nivel_1, self.percentual_nivel_2, self.percentual_nivel_3, self.percentual_nivel_4, self.aliquota_nivel_1, self.aliquota_nivel_2, self.aliquota_nivel_3, self.aliquota_nivel_4)
       
        self.hipoteca_valida_01 = hipoteca.Hipoteca(self.descricao, self.valor_casa, self.valor_entrada_01, self.tabelaSeguro, self.tvq_valida, self.taxa_juros_01)
        self.hipoteca_valida_02 = hipoteca.Hipoteca(self.descricao, self.valor_casa, self.valor_entrada_02, self.tabelaSeguro, self.tvq_valida, self.taxa_juros_01)
        self.hipoteca_valida_03 = hipoteca.Hipoteca(self.descricao, self.valor_casa, self.valor_entrada_03, self.tabelaSeguro, self.tvq_valida, self.taxa_juros_01)
        self.hipoteca_valida_04 = hipoteca.Hipoteca(self.descricao, self.valor_casa, self.valor_entrada_04, self.tabelaSeguro, self.tvq_valida, self.taxa_juros_01)        
        
    def test_init(self):
        self.assertEqual(self.hipoteca_valida_01.valor_casa, self.valor_casa)
        self.assertEqual(self.hipoteca_valida_01.valor_entrada, self.valor_entrada_01)
        self.assertEqual(self.hipoteca_valida_01.tvq, self.tvq_valida)
        self.assertEqual(self.hipoteca_valida_01.tabelaSeguro, self.tabelaSeguro)
        self.assertEqual(self.hipoteca_valida_01.taxa_juros, self.taxa_juros_01)
    
    def test_validar_config_01(self):
        with self.assertRaises(ValueError):
            # entrada menor que 5%
            self.hipoteca_invalida_01 = hipoteca.Hipoteca(self.descricao, self.valor_casa, self.valor_entrada_invalida_02, self.tabelaSeguro, self.tvq_valida, self.taxa_juros_01)
    
    def test_validar_config_02(self):
        with self.assertRaises(ValueError):
            #entrada maior que valor da casa
            self.hipoteca_invalida_01 = hipoteca.Hipoteca(self.descricao, self.valor_casa, self.valor_entrada_invalida_01, self.tabelaSeguro, self.tvq_valida, self.taxa_juros_01)
    
    def test_validar_config_03(self):
        with self.assertRaises(ValueError):
            #tvq maior que 100
            self.hipoteca_invalida_01 = hipoteca.Hipoteca(self.descricao, self.valor_casa, self.valor_entrada_04, self.tabelaSeguro, self.tvq_invalida_01, self.taxa_juros_01)

    def test_validar_config_04(self):
        with self.assertRaises(ValueError):
            #tvq menor do que zero
            self.hipoteca_invalida_01 = hipoteca.Hipoteca(self.descricao, self.valor_casa, self.valor_entrada_04, self.tabelaSeguro, self.tvq_invalida_02, self.taxa_juros_01)
    
    def test_validar_config_05(self):
        with self.assertRaises(ValueError):
            #tvq menor do que zero
            self.hipoteca_invalida_01 = hipoteca.Hipoteca(self.descricao, self.valor_casa, self.valor_entrada_04, self.tabelaSeguro, self.tvq_valida, self.taxa_juros_invalida)

    def test_calcular_percentual_entrada(self):
        self.assertEqual(self.hipoteca_valida_01.calcular_percentual_entrada(), self.percentual_entrada_1)
        self.assertEqual(self.hipoteca_valida_02.calcular_percentual_entrada(), self.percentual_entrada_2)
        self.assertEqual(self.hipoteca_valida_03.calcular_percentual_entrada(), self.percentual_entrada_3)
        self.assertEqual(self.hipoteca_valida_04.calcular_percentual_entrada(), self.percentual_entrada_4)

    def test_calcular_valor_financiado(self):
        self.assertEqual(self.hipoteca_valida_01.calcular_valor_financiado(), self.valor_financiado_1)
        self.assertEqual(self.hipoteca_valida_02.calcular_valor_financiado(), self.valor_financiado_2)
        self.assertEqual(self.hipoteca_valida_03.calcular_valor_financiado(), self.valor_financiado_3)
        self.assertEqual(self.hipoteca_valida_04.calcular_valor_financiado(), self.valor_financiado_4)
    
    def test_calcular_percentual_seguro(self):
        self.assertEqual(self.hipoteca_valida_01.calcular_percentual_seguro(), self.aliquota_nivel_4)
        self.assertEqual(self.hipoteca_valida_02.calcular_percentual_seguro(), self.aliquota_nivel_2)
        self.assertEqual(self.hipoteca_valida_03.calcular_percentual_seguro(), self.aliquota_nivel_1)
        self.assertEqual(self.hipoteca_valida_04.calcular_percentual_seguro(), self.aliquota_nivel_3)

    def test_calcular_valor_seguro(self):
        self.assertEqual(self.hipoteca_valida_01.calcular_valor_seguro(), self.valor_seguro_1)
        self.assertEqual(self.hipoteca_valida_02.calcular_valor_seguro(), self.valor_seguro_2)
        self.assertEqual(self.hipoteca_valida_03.calcular_valor_seguro(), self.valor_seguro_3)
        self.assertEqual(self.hipoteca_valida_04.calcular_valor_seguro(), self.valor_seguro_4)