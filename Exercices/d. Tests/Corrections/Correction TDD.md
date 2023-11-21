
```python
import unittest

def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

class TestCalculateAverage(unittest.TestCase):
    def test_calculate_average(self):
        # Test avec une liste de nombres entiers
        self.assertEqual(calculate_average([1, 2, 3]), 2)

        # Test avec une liste de nombres décimaux
        self.assertEqual(calculate_average([2.5, 3.5, 4.5]), 3.5)

        # Test avec une liste vide
        self.assertIsNone(calculate_average([]))

if __name__ == '__main__':
    unittest.main()
```
