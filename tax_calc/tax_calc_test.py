import unittest

from tax_calc import filing_status, tax_calc


class TaxCalcTest(unittest.TestCase):

    def test_tax_calc_for_no_income(self):
        self.assertEqual(tax_calc.calculate_tax(
            filing_status.FilingStatus.SINGLE, 0), 0)

    def test_tax_calc_for_one_bracket(self):
        self.assertEqual(tax_calc.calculate_tax(
            filing_status.FilingStatus.SINGLE, 9000), 900)

    def test_tax_calc_for_multiple_brackets(self):
        self.assertEqual(tax_calc.calculate_tax(
            filing_status.FilingStatus.SINGLE, 200000), 44827)

    def test_tax_calc_for_top_bracket(self):
        self.assertEqual(tax_calc.calculate_tax(
            filing_status.FilingStatus.SINGLE, 1000000), 334072.25)

    def test_tax_calc_for_differnet_filing_status(self):
        self.assertEqual(tax_calc.calculate_tax(
            filing_status.FilingStatus.MARRIED_FILING_JOINTLY, 400000), 89654)


if __name__ == '__main__':
    unittest.main()
