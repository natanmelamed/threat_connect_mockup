import options
from common.dto_decoder import DtoEncoder
from common import data_generator
from datetime import datetime, timedelta


@DtoEncoder
class AttributeDto:
    def __init__(self):
        attribute_map: dict = data_generator.random_from_list(options.ATTRIBUTE_MAP)
        self.id: int = int(data_generator.random_digits_string(7))
        self.type: str = list((attribute_map.keys()))[0]
        self.value: str = attribute_map[self.type]
        self.dateAdded: str = \
            str((datetime.now() + timedelta(seconds=3)).strftime(options.TIME_FORMAT))
        self.lastModified: str = \
            str((datetime.now() + timedelta(seconds=3)).strftime(options.TIME_FORMAT))
        self.displayed: bool = data_generator.random_from_list(options.BOOL_VALUES)
        self.xid: str = f"f73e684c-11b2-4c38-a29a-8eb759b25c5b:{self.id}"
