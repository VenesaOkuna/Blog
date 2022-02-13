import unittest
from models import random_quote
Random_Quote = random_quote.Random_Quote

class Random_QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Random_Quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_random_quote = Random_Quote(43,"There are only two hard things in Computer Science: cache invalidation, naming things and off-by-one errors.","Phil Karlton",8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_random_quote,Random_Quote))


if __name__ == '__main__':
    unittest.main()