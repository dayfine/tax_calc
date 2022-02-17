from tax_calc import filing_status as fs, tax_brackets


def calculate_tax(filing_status: fs.FilingStatus,
                  taxable_income: int) -> float:

    brackets = tax_brackets.TAX_BRACKETS_2021[filing_status]
    result = 0
    lower_limt = 0
    for bracket in brackets:
        result += bracket.rate * \
            (min(taxable_income, bracket.uppper_limit or float('inf')) - lower_limt)

        lower_limt = bracket.uppper_limit

        if bracket.uppper_limit and taxable_income <= bracket.uppper_limit:
            break

    return result
