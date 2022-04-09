import unittest
import tabelaseguro

class TestTabelaSeguro(unittest.TestCase):

    def test_init(self):
        tabelaSeguro = tabelaseguro.TabelaSeguro(10, 15, 20, 100, 4.0, 3.1, 2.8, 0)
        self.assertEqual(tabelaSeguro.percentual_nivel_1, 10)
        self.assertEqual(tabelaSeguro.percentual_nivel_2, 15)
        self.assertEqual(tabelaSeguro.percentual_nivel_3, 20)
        self.assertEqual(tabelaSeguro.percentual_nivel_4, 100)
        self.assertEqual(tabelaSeguro.aliquota_nivel_1, 4.0)
        self.assertEqual(tabelaSeguro.aliquota_nivel_2, 3.1)
        self.assertEqual(tabelaSeguro.aliquota_nivel_3, 2.8)
        self.assertEqual(tabelaSeguro.aliquota_nivel_4, 0)

    def test_calcular_percentual_entrada(self):
        tabelaSeguro = tabelaseguro.TabelaSeguro(10, 15, 20, 100, 4.0, 3.1, 2.8, 0)
        self.assertEqual(tabelaSeguro.calcular_percentual_seguro(percentual_entrada = 5.0), 4.0)
        self.assertEqual(tabelaSeguro.calcular_percentual_seguro(percentual_entrada = 10.0), 3.1)
        self.assertEqual(tabelaSeguro.calcular_percentual_seguro(percentual_entrada = 15.0), 2.8)
        self.assertEqual(tabelaSeguro.calcular_percentual_seguro(percentual_entrada = 20.0), 0)
        self.assertEqual(tabelaSeguro.calcular_percentual_seguro(percentual_entrada = 25.0), 0)