# import unittest
from lib.fizzbuzz import FizzBuzz
from unittest.mock import MagicMock, patch

class TestFizzBuzz:

    def test_check_number(self):
         check = FizzBuzz(45)
         assert check.check_number(15) == "fizzbuzz"
         assert check.check_number(3) == "fizz"
         assert check.check_number(5) == "buzz"
         assert check.check_number(1) == 1

    def test_run(self):
        # with patch.object(FizzBuzz, "check_number") as mock_method:
             RUN_TIMES = 45
             check = FizzBuzz(RUN_TIMES)
             check.check_number = MagicMock()
             check.run()
             assert check.check_number.call_count == RUN_TIMES - 1