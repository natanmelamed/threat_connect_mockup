import options
from common.dto_decoder import DtoEncoder
from common import data_generator
from datetime import datetime, timedelta


@DtoEncoder
class AssociatedGroupDto:
    def __init__(self):
        self.id: int = int(data_generator.random_digits_string(7))
        self.name: str = data_generator.random_string_in_range(10, 15)
        self.type: str = data_generator.random_from_list(options.ASSOCIATED_GROUP_TYPES)
        self.ownerName: str = "CyberProof"
        self.dateAdded: str = \
            str((datetime.now() + timedelta(seconds=3)).strftime(options.TIME_FORMAT))
        url_type: str = self.type.lower()
        self.webLink: str = f"https://testowner.tc.com/auth/{url_type}/{url_type}.xhtml?" \
                            f"{url_type}={self.id}"
