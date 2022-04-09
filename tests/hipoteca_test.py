import unittest
import hipoteca
import tabelaseguro

class TestHipoteca(unittest.TestCase):

    def setUp(self):
        self.tabelaSeguro = tabelaseguro.TabelaSeguro(10, 15, 20, 100, 4.0, 3.1, 2.8, 0)
        self.hipoteca_valida_01 = hipoteca.Hipoteca(400000, 80000, self.tabelaSeguro, 9.0)
        self.hipoteca_valida_02 = hipoteca.Hipoteca(400000, 40000, self.tabelaSeguro, 9.0)
        self.hipoteca_valida_03 = hipoteca.Hipoteca(400000, 30000, self.tabelaSeguro, 9.0)
        self.hipoteca_valida_04 = hipoteca.Hipoteca(400000, 60000, self.tabelaSeguro, 9.0)
        self.hipoteca_invalida_01 = hipoteca.Hipoteca(400000, 600, self.tabelaSeguro, 9.0)

    def test_init(self):
        self.assertEqual(self.hipoteca_valida_01.valor_casa, 400000)
        self.assertEqual(self.hipoteca_valida_01.valor_entrada, 80000)
        self.assertEqual(self.hipoteca_valida_01.tvq, 9.0)
        self.assertEqual(self.hipoteca_valida_01.tabelaSeguro, self.hipoteca_valida_01.tabelaSeguro)
    
    def test_validar_config(self):
        with self.assertRaises(ValueError):
            self.hipoteca_invalida_01.validar_config()

    def test_abc(self):
        with self.assertRaises(ZeroDivisionError):
            100/0

    def test_calcular_percentual_entrada(self):
        self.assertEqual(self.hipoteca_valida_01.calcular_percentual_entrada(),20.0)
        self.assertEqual(self.hipoteca_valida_02.calcular_percentual_entrada(),10.0)
        self.assertEqual(self.hipoteca_valida_03.calcular_percentual_entrada(),7.5)
        self.assertEqual(self.hipoteca_valida_04.calcular_percentual_entrada(),15)

    def test_calcular_valor_financiado(self):
        self.assertEqual(self.hipoteca_valida_01.calcular_valor_financiado(), (400000 - 80000) + (400000 * 0 / 100))
        self.assertEqual(self.hipoteca_valida_02.calcular_valor_financiado(), (400000 - 40000) + (400000 * 3.1 / 100))
        self.assertEqual(self.hipoteca_valida_03.calcular_valor_financiado(), (400000 - 30000) + (400000 * 4.0 / 100))
        self.assertEqual(self.hipoteca_valida_04.calcular_valor_financiado(), (400000 - 60000) + (400000 * 2.8 / 100))
    
    def test_calcular_percentual_seguro(self):
        self.assertEqual(self.hipoteca_valida_01.calcular_percentual_seguro(), 0)
        self.assertEqual(self.hipoteca_valida_02.calcular_percentual_seguro(), 3.1)
        self.assertEqual(self.hipoteca_valida_03.calcular_percentual_seguro(), 4.0)
        self.assertEqual(self.hipoteca_valida_04.calcular_percentual_seguro(), 2.8)

    def test_calcular_valor_seguro(self):
        self.assertEqual(self.hipoteca_valida_01.calcular_valor_seguro(), 0   / 100 * 400000)
        self.assertEqual(self.hipoteca_valida_02.calcular_valor_seguro(), 3.1 / 100 * 400000)
        self.assertEqual(self.hipoteca_valida_03.calcular_valor_seguro(), 4.0 / 100 * 400000)
        self.assertEqual(self.hipoteca_valida_04.calcular_valor_seguro(), 2.8 / 100 * 400000)

