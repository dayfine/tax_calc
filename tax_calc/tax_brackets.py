import dataclasses
from typing import Mapping, NewType, Optional, Tuple

from tax_calc import filing_status as fs


@dataclasses.dataclass
class TaxBracket:
    # Taxable rate for ordinary income.
    # For simplicity, this model doesn't support qualified rate for long term capital gain
    # and qualified dividends.
    rate: float
    # The upper limit for a given tax bracket.
    # None for the top bracket.
    uppper_limit: Optional[int]


TaxBracketsByFilingStatus = NewType('TaxBracketsByFilingStatus',
                                    Mapping[fs.FilingStatus,  Tuple[TaxBracket, ...]])


TAX_BRACKETS_2021: TaxBracketsByFilingStatus = {
    fs.FilingStatus.SINGLE: [
        TaxBracket(.10, 9950),
        TaxBracket(.12, 40525),
        TaxBracket(.22, 86375),
        TaxBracket(.24, 164925),
        TaxBracket(.32, 209425),
        TaxBracket(.35, 523600),
        TaxBracket(.37, None),
    ],
    fs.FilingStatus.MARRIED_FILING_JOINTLY: [
        TaxBracket(.10, 19900),
        TaxBracket(.12, 81050),
        TaxBracket(.22, 172750),
        TaxBracket(.24, 329850),
        TaxBracket(.32, 418850),
        TaxBracket(.35, 628300),
        TaxBracket(.37, None),
    ],
    fs.FilingStatus.MARRIED_FILING_SEPARATELY: [
        TaxBracket(.10, 9950),
        TaxBracket(.12, 40525),
        TaxBracket(.22, 86375),
        TaxBracket(.24, 164925),
        TaxBracket(.32, 209425),
        TaxBracket(.35, 314150),
        TaxBracket(.37, None),
    ],
    fs.FilingStatus.HEAD_OF_HOUSEHOLD: [
        TaxBracket(.10, 14200),
        TaxBracket(.12, 54200),
        TaxBracket(.22, 86350),
        TaxBracket(.24, 164900),
        TaxBracket(.32, 209400),
        TaxBracket(.35, 523600),
        TaxBracket(.37, None),
    ],
}
