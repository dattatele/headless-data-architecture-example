import unittest
from flink_python.main import main

class TestFlinkJob(unittest.TestCase):
    def test_flink_job(self):
        # Test to ensure that Flink job runs without exceptions
        try:
            main()
        except Exception as e:
            self.fail(f"main() raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()