import unittest
class SystemUnderTest:
    def __init__(self):
        self.easter_egg_enabled = True

    def process_input(self, input_value):
        if self.easter_egg_enabled and input_value == '1015':
            return '[EVENT] 기념일입니다.'
        else:
            return 'Regular Processing'

class EasterEggTest(unittest.TestCase):
    def setUp(self):
        self.system = SystemUnderTest()

    def test_easter_egg_accuracy(self):
        result = self.system.process_input('1015')
        self.assertEqual(result, '[EVENT] 기념일입니다.')

    def test_non_easter_egg_number(self):
        result = self.system.process_input('1234')
        self.assertNotEqual(result, '[EVENT] 기념일입니다.')

    def test_invalid_input(self):
        result = self.system.process_input('abcd')
        self.assertNotEqual(result, '[EVENT] 기념일입니다.')

    def test_boundary_value(self):
        result_1014 = self.system.process_input('1014')
        result_1016 = self.system.process_input('1016')
        self.assertNotEqual(result_1014, '[EVENT] 기념일입니다.')
        self.assertNotEqual(result_1016, '[EVENT] 기념일입니다.')

    def test_easter_egg_disabled(self):
        self.system.easter_egg_enabled = False
        result = self.system.process_input('1015')
        self.assertNotEqual(result, '[EVENT] 기념일입니다.')

if __name__ == '__main__':
    unittest.main()
