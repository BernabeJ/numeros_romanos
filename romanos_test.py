import unittest
import romanos
import romanos_kata

class RomanNumberTest(unittest.TestCase):
    
    def test_symbols_romans(self):
        self.assertEqual(romanos_kata.romano_a_entero('I'),1)
        self.assertEqual(romanos_kata.romano_a_entero('V'),5)
        self.assertEqual(romanos_kata.romano_a_entero('X'),10)
        self.assertEqual(romanos_kata.romano_a_entero('L'),50)
        self.assertEqual(romanos_kata.romano_a_entero('C'),100)
        self.assertEqual(romanos_kata.romano_a_entero('K'),'Error en formato')
        self.assertEqual(romanos_kata.romano_a_entero(''),'Error en formato')



    def test_repetitions(self):
        self.assertEqual(romanos_kata.romano_a_entero('II'),2)
        self.assertEqual(romanos_kata.romano_a_entero('MMM'),3000)
        self.assertEqual(romanos_kata.romano_a_entero('KKK'),'Error en formato')
        self.assertEqual(romanos_kata.romano_a_entero('MK'),'Error en formato')
    
    def test_only_three(self):
        self.assertEqual(romanos_kata.romano_a_entero('IIII'),'Error en formato')
    
    def test_numeros_decrecientes(self):
        self.assertEqual(romanos_kata.romano_a_entero('XVIII'), 18)
        self.assertEqual(romanos_kata.romano_a_entero('IL'),'Error en formato')

class IntergerToRomanTest(unittest.TestCase):
    def test_traduccion_digitos(self):
        self.assertEqual(romanos_kata.entero_a_romano(1),'I')
        self.assertEqual(romanos_kata.entero_a_romano(10),'X')
        self.assertEqual(romanos_kata.entero_a_romano(5),'V')
        self.assertEqual(romanos_kata.entero_a_romano(50),'L')
        self.assertEqual(romanos_kata.entero_a_romano(100),'C')
        self.assertEqual(romanos_kata.entero_a_romano(500),'D')
        self.assertEqual(romanos_kata.entero_a_romano(1000),'M')
        self.assertEqual(romanos_kata.entero_a_romano(30),'XXX')
        self.assertEqual(romanos_kata.entero_a_romano(400),'CD')
        self.assertEqual(romanos_kata.entero_a_romano(3000),'MMM')

    def test_busca_valor(self):
        self.assertEqual(romanos_kata.busca_valor_menor_o_igual(2), ('I',1))
        self.assertEqual(romanos_kata.busca_valor_menor_o_igual(5), ('V',5))
        self.assertEqual(romanos_kata.busca_valor_menor_o_igual(7), ('V',5))
    
    def test_descomponer(self):
        self.assertEqual(romanos_kata.descomponer(1492), [1000,400,90,2])

    def test_entero_a_romano(self):
        self.assertEqual(romanos_kata.entero_a_romano(1492), 'MCDXCII')
        self.assertEqual(romanos_kata.entero_a_romano(3999), 'MMMCMXCIX')
        self.assertEqual(romanos_kata.entero_a_romano(4000),'Overflow')

        

if __name__ == '__main__':
    unittest.main()
