import unittest

class TestSystemErrorOutput(unittest.TestCase):
    
    def simulate_error(self):
        return "[SYSTEM] \"ERROR!\""

    def test_error_format(self):
        expected_format = "[SYSTEM] \"ERROR!\""
        error_message = self.simulate_error()
        self.assertEqual(error_message, expected_format, "에러 메시지 형식이 올바르지 않습니다.")

    def test_error_inclusion(self):
        error_message = self.simulate_error()
        self.assertIn("SYSTEM", error_message, "'SYSTEM'이 에러 메시지에 포함되어 있지 않습니다.")
        self.assertIn("ERROR", error_message, "'ERROR'가 에러 메시지에 포함되어 있지 않습니다.")

if __name__ == '__main__':
    unittest.main()
