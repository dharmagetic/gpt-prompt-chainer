import logging
import unittest

# Set up logging configuration
logging.basicConfig(level=logging.INFO)


class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            return self._successor.handle(request)
        return None


class FizzBuzzHandler(Handler):
    def handle(self, request):
        if request % 3 == 0 and request % 5 == 0:
            logging.info("Handled by FizzBuzzHandler")
            return "FizzBuzz"
        return super().handle(request)


class FizzHandler(Handler):
    def handle(self, request):
        if request % 3 == 0:
            logging.info("Handled by FizzHandler")
            return "Fizz"
        return super().handle(request)


class BuzzHandler(Handler):
    def handle(self, request):
        if request % 5 == 0:
            logging.info("Handled by BuzzHandler")
            return "Buzz"
        return super().handle(request)


class DefaultHandler(Handler):
    def handle(self, request):
        logging.info("Handled by DefaultHandler")
        return str(request)


def fizzbuzz(n):
    """
    Generates a list of numbers from 1 to n, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both 3 and 5 with "FizzBuzz".

    Args:
        n (int): The upper limit of the range starting from 1.

    Returns:
        list: A list of strings representing the FizzBuzz output.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    handler_chain = FizzBuzzHandler(FizzHandler(BuzzHandler(DefaultHandler())))
    result = []
    for i in range(1, n + 1):
        result.append(handler_chain.handle(i))
    return result


if __name__ == "__main__":
    n = 100
    try:
        fizzbuzz_result = fizzbuzz(n)
        print(fizzbuzz_result)
    except ValueError as e:
        print(e)


# Unit tests to validate the implementation
class TestFizzBuzzHandlers(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz_handler = FizzBuzzHandler(
            FizzHandler(BuzzHandler(DefaultHandler()))
        )

    def test_fizzbuzz_handler(self):
        self.assertEqual(self.fizzbuzz_handler.handle(15), "FizzBuzz")
        self.assertEqual(self.fizzbuzz_handler.handle(3), "Fizz")
        self.assertEqual(self.fizzbuzz_handler.handle(5), "Buzz")
        self.assertEqual(self.fizzbuzz_handler.handle(7), "7")

    def test_fizzbuzz_function(self):
        expected_output = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
            "16",
            "17",
            "Fizz",
            "19",
            "Buzz",
        ]
        self.assertEqual(fizzbuzz(20), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            fizzbuzz(-1)
        with self.assertRaises(ValueError):
            fizzbuzz(0)
        with self.assertRaises(ValueError):
            fizzbuzz("a")


if __name__ == "__main__":
    unittest.main()
