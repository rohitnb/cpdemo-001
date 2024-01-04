import unittest 
import sys
import calcfunctions 

from calcfunctions import addInputs, subtractInputs, multiplyInputs, divideInputs, modInputs, powerInputs  
  
  
class CheckSum(unittest.TestCase):  
    def test_addinputs(self):  
  
        input1 = 1
        input2 = 2
        result = addInputs(input1, input2)  
        self.assertEqual(result, 3)  
    
    def test_subtractinputs(self):  
  
        input1 = 1
        input2 = 2
        result = subtractInputs(input1, input2)  
        self.assertEqual(result, -1)
    
    def test_multiplyinputs(self):  
  
        input1 = 1
        input2 = 2
        result = multiplyInputs(input1, input2)  
        self.assertEqual(result, 2)

    def test_divideinputs(self):  
  
        input1 = 16
        input2 = 2
        result = divideInputs(input1, input2)  
        self.assertEqual(result, 8)
    
    def test_modinputs(self):
        input1 = 16
        input2 = 2
        result = modInputs(input1, input2)  
        self.assertEqual(result, 0)
    
    def test_powerinputs(self):
        input1 = 2
        input2 = 2
        result = powerInputs(input1, input2)  
        self.assertEqual(result, 4)

if __name__ == '__main__':  
    unittest.main() 