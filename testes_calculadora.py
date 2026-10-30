"""
Script de testes automatizados para a Calculadora (CalculaPy.py).
Utiliza o framework padrão 'unittest' do Python.

Para executar estes testes no terminal, digite:
    python testes_calculadora.py
"""

import math
import os
import sys
import unittest

# Garante que o diretório atual do arquivo esteja no sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from CalculaPy import (
    somar,
    subtrair,
    multiplicar,
    dividir,
    calcular_porcentagem,
    calcular_escala,
    regra_de_tres,
    calcular_probabilidade,
    area_retangulo,
    area_quadrado,
    area_triangulo,
    area_triangulo_equilatero,
    circulo_area_comprimento,
    area_trapezio,
    teorema_pitagoras,
    volume_paralelepipedo,
    volume_cilindro,
    volume_esfera,
    relacao_euler,
)


class TestOperacoesBasicas(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(somar(10, 5), 15)
        self.assertEqual(somar(-2, 3), 1)

    def test_subtracao(self):
        self.assertEqual(subtrair(20, 8), 12)

    def test_multiplicacao(self):
        self.assertEqual(multiplicar(7, 6), 42)

    def test_divisao_normal(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(7, 2), 3.5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)


class TestOperacoesAvancadas(unittest.TestCase):
    def test_porcentagem(self):
        # 15% de 200 = 30
        self.assertEqual(calcular_porcentagem(15, 200), 30)

    def test_escala(self):
        # 2 cm no mapa para 1000 cm reais -> Escala 1:500
        self.assertEqual(calcular_escala(2, 1000), 500)
        with self.assertRaises(ValueError):
            calcular_escala(0, 100)

    def test_regra_de_tres(self):
        # 2 está para 10, assim como 4 está para X -> X = 20
        self.assertEqual(regra_de_tres(2, 10, 4), 20)
        with self.assertRaises(ZeroDivisionError):
            regra_de_tres(0, 10, 4)

    def test_probabilidade(self):
        # 1 caso em 4 -> 0.25 (25%)
        self.assertAlmostEqual(calcular_probabilidade(1, 4), 0.25)
        with self.assertRaises(ZeroDivisionError):
            calcular_probabilidade(1, 0)
        with self.assertRaises(ValueError):
            calcular_probabilidade(5, 2)  # Casos favoráveis maiores que o total


class TestGeometriaPlana(unittest.TestCase):
    def test_area_retangulo(self):
        self.assertEqual(area_retangulo(5, 10), 50)

    def test_area_quadrado(self):
        self.assertEqual(area_quadrado(7), 49)

    def test_area_triangulo(self):
        self.assertEqual(area_triangulo(8, 5), 20)

    def test_area_triangulo_equilatero(self):
        # Lado 2 -> (4 * sqrt(3)) / 4 = sqrt(3)
        self.assertAlmostEqual(area_triangulo_equilatero(2), math.sqrt(3))

    def test_circulo(self):
        area, comp = circulo_area_comprimento(3)
        self.assertAlmostEqual(area, math.pi * 9)
        self.assertAlmostEqual(comp, 2 * math.pi * 3)

    def test_area_trapezio(self):
        # B=10, b=6, h=4 -> ((10 + 6) * 4) / 2 = 32
        self.assertEqual(area_trapezio(10, 6, 4), 32)

    def test_pitagoras(self):
        # Triângulo clássico 3, 4, 5
        self.assertEqual(teorema_pitagoras(3, 4), 5)


class TestGeometriaEspacial(unittest.TestCase):
    def test_volume_paralelepipedo(self):
        self.assertEqual(volume_paralelepipedo(2, 3, 4), 24)

    def test_volume_cilindro(self):
        # Raio 2, Altura 5 -> pi * 4 * 5 = 20*pi
        self.assertAlmostEqual(volume_cilindro(2, 5), 20 * math.pi)

    def test_volume_esfera(self):
        # Raio 3 -> (4/3) * pi * 27 = 36*pi
        self.assertAlmostEqual(volume_esfera(3), 36 * math.pi)

    def test_relacao_euler_calculo_faces(self):
        # Cubo: V=8, A=12 -> F deve ser 6
        resultado = relacao_euler(8, 12, 0)
        self.assertIn("Faces (F) = 6", resultado)

    def test_relacao_euler_calculo_arestas(self):
        # Icosaedro: V=12, F=20 -> A deve ser 30
        resultado = relacao_euler(12, 0, 20)
        self.assertIn("Arestas (A) = 30", resultado)

    def test_relacao_euler_validacao(self):
        # Cubo com todos os valores informados
        resultado = relacao_euler(8, 12, 6)
        self.assertIn("Poliedro Convexo Válido", resultado)


if __name__ == "__main__":
    unittest.main()
