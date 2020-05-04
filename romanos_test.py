import unittest
import romanos

class RomanNumberTest(unittest.TestCase):
    
    def test_symbols_romans(self):
        self.assertEqual(romanos.romano_a_entero('I'),1)
        self.assertEqual(romanos.romano_a_entero('V'),5)
        self.assertEqual(romanos.romano_a_entero('X'),10)
        self.assertEqual(romanos.romano_a_entero('L'),50)
        self.assertEqual(romanos.romano_a_entero('C'),100)
        self.assertEqual(romanos.romano_a_entero('K'),'caracter no valido')
        self.assertEqual(romanos.romano_a_entero(''),'caracter no valido')



    def test_repetitions(self):
        self.assertEqual(romanos.romano_a_entero('II'),2)
        self.assertEqual(romanos.romano_a_entero('MMM'),3000)
        self.assertEqual(romanos.romano_a_entero('KKK'),'caracter no valido')
        self.assertEqual(romanos.romano_a_entero('MK'),'caracter no valido')
    
    def test_only_three(self):
        self.assertEqual(romanos.romano_a_entero('IIII'),'Error de formato')
    
    def test_numeros_decrecientes(self):
        self.assertEqual(romanos.romano_a_entero('XVIII'), 18)
        self.assertEqual(romanos.romano_a_entero('IL'),'Error en formato')
        

if __name__ == '__main__':
    unittest.main()
