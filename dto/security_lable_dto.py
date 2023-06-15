from common.dto_decoder import DtoEncoder
import options
from datetime import datetime, timedelta
from common import data_generator


@DtoEncoder
class SecurityLabelDto:
    def __init__(self):
        self.name: str = "TLP:" + data_generator.random_string_in_range()
        self.description: str = "Description " + data_generator.random_string_in_range(15, 20)
        self.dateAdded: str = \
            str((datetime.now() + timedelta(seconds=3)).strftime(options.TIME_FORMAT))
