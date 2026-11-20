
import unittest
from budget import FeatureBudget


class TestFeatureBudget(unittest.TestCase):

    def setUp(self):
        self.budget = FeatureBudget(
            requests_per_day=100,
            avg_input_tokens=1000,
            avg_output_tokens=500,
            peak_requests_per_minute=10,
            input_price_per_million=0.30,
            output_price_per_million=1.20,
            rpm_limit=20,
            tpm_limit=20000,
            monthly_budget_usd=10,
            daily_budget_usd=0.20,
            safety_margin_percent=20
        )

    def test_token_calculation(self):
        result = self.budget.calculate()
        self.assertEqual(result["input_tokens_day"], 100000)
        self.assertEqual(result["output_tokens_day"], 50000)
        self.assertEqual(result["total_tokens_day"], 150000)

    def test_daily_cost(self):
        result = self.budget.calculate()
        self.assertAlmostEqual(result["daily_cost_usd"], 0.09)

    def test_monthly_cost(self):
        result = self.budget.calculate()
        self.assertAlmostEqual(result["monthly_cost_usd"], 2.70)

    def test_rpm_limit(self):
        result = self.budget.calculate()
        self.assertTrue(result["rpm_ok"])

    def test_tpm_limit(self):
        result = self.budget.calculate()
        self.assertTrue(result["tpm_ok"])


if __name__ == "__main__":
    unittest.main()
