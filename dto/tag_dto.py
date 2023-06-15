from common import data_generator
from common.dto_decoder import DtoEncoder


@DtoEncoder
class TagDto:
    def __init__(self):
        self.name: str = data_generator.random_string_in_range(10, 15)
        self.webLink: str = f"https://testowner.tc.com/auth/tags/tag.xhtml?tag=" \
                            f"{self.name}&owner=CyberProof"
