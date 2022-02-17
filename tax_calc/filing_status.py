import enum

class FilingStatus(enum.Enum):
    SINGLE = enum.auto()
    MARRIED_FILING_JOINTLY = enum.auto()
    MARRIED_FILING_SEPARATELY = enum.auto()
    HEAD_OF_HOUSEHOLD = enum.auto()