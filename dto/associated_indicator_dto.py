import options
from common.dto_decoder import DtoEncoder
from common import data_generator
from datetime import datetime, timedelta


@DtoEncoder
class AssociatedIndicatorDto:
    def __init__(self):
        indicator_map: dict = data_generator.random_from_list(options.ASSOCIATED_INDICATOR_MAP)
        self.id: int = int(data_generator.random_digits_string(7))
        self.ownerName: str = "CyberProof"
        self.type: str = list((indicator_map.keys()))[0]
        self.dateAdded: str = \
            str((datetime.now() + timedelta(seconds=3)).strftime(options.TIME_FORMAT))
        self.lastModified: str = \
            str((datetime.now() + timedelta(seconds=3)).strftime(options.TIME_FORMAT))
        self.threatAssessRating: float = data_generator.random_float_in_range()
        self.threatAssessConfidence: float = data_generator.random_float_in_range()
        url_type: str = self.type.lower()
        self.webLink: str = f"https://testowner.tc.com/auth/indicators/details/" \
                            f"{url_type}.xhtml?{url_type}={self.id}"
        self.description: str = "Mock description " + data_generator.random_string_in_range(10, 15)
        self.summary: str = indicator_map[self.type]
