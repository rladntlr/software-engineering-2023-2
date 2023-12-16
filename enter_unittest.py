import unittest
class MockCalculator:
    def __init__(self):
        self.inputs = []
        self.result = None

    def enter(self, input):
        if input == 'Enter':
            return self.result
        elif input == '=':
            self.calculate()
        else:
            self.inputs.append(input)
        return None

    def calculate(self):
        if len(self.inputs) != 3 or self.inputs[1] != '+':
            self.result = 'Error'
        else:
            try:
                self.result = str(int(self.inputs[0]) + int(self.inputs[2]))
            except ValueError:
                self.result = 'Error'
        self.inputs = []  # 입력 초기화


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

if __name__ == '__main__':
    unittest.main()
