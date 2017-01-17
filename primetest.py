import  unittest
import random


class primeCheck(unittest.TestCase):
    def test_prime(self):
        #"""find_prime should always return True for numbers divisible by itself == 0"""
        random_integer = random.randint(0,1000)
        a = random_integer/random_integer
        self.assertEqual((a == int(a)),even.find_prime(random_integer), "wrong answer for "+str(random_integer))


        
class test_input(unittest.TestCase):
    
    
        
    def test_nonInteger(self):
        "find_even should only accept integers only"
        l = ['a','2.0']
        for a in l:
            self.assertRaises(even.NonIntegerError, even.find_even, a )
    
if __name__ == "__main__":
    unittest.main()
        
