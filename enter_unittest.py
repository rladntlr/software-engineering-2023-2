import unittest

class MockCalculator:
    def enter(self, input):
        pass

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = MockCalculator()
def test_number_and_operator_input_with_enter(self):
    self.calc.enter('3')
    self.calc.enter('+')
    self.calc.enter('5')
    self.calc.enter('=')
    result = self.calc.enter('Enter')
    self.assertEqual(result, '8')
def test_ignore_inputs_without_enter(self):
    self.calc.enter('3')
    self.calc.enter('+')
    self.calc.enter('5')
    self.calc.enter('=')
    result = self.calc.enter('Enter')
    self.assertIsNone(result)
def test_operator_input_requires_enter(self):
    self.calc.enter('3')
    self.calc.enter('+')
    result = self.calc.enter('Enter')
    self.assertIsNone(result)  
def test_output_after_enter_post_equals(self):
    self.calc.enter('3')
    self.calc.enter('+')
    self.calc.enter('5')
    self.calc.enter('=')
    result = self.calc.enter('Enter')
    self.assertEqual(result, '8')
def test_invalid_input_after_enter(self):
    result = self.calc.enter('a')
    self.assertIn(result, [None, 'Error'])  
if __name__ == '__main__':
    unittest.main()