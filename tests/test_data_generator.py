import unittest
from data_generator.generate_data import generate_sales_data

class TestDataGenerator(unittest.TestCase):
    def test_generate_sales_data(self):
        # Test to ensure that generate_sales_data runs without exceptions
        try:
            generate_sales_data()
        except Exception as e:
            self.fail(f"generate_sales_data() raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()