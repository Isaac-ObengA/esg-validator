import unittest
from esgvalidator import validator
class TestValidator(unittest.TestCase):
    def test_valid_data(self):
        data = {
            "emissions": "10t",
            "energy_use": "Hydro",
            "governance_score": "A" }
        result = validator.validate_and_hash(data)
        self.assertEqual(result["status"], "pass")
def test_missing_fields(self):
        data = { "emissions": "10t" }
        result = validator.validate_and_hash(data)
        self.assertEqual(result["status"], "fail")
        self.assertIn("energy_use", result["errors"])
if __name__ == '__main__':
    unittest.main()
