import unittest
from agent import summarize_comparables


class ValuationTests(unittest.TestCase):
    def test_missing_comparables_abstains(self):
        result = summarize_comparables({"area_sqft": 1000}, [])
        self.assertEqual(result["status"], "insufficient-evidence")
        self.assertIsNone(result["formal_valuation"])


if __name__ == "__main__":
    unittest.main()
