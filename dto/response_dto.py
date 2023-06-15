from common.dto_decoder import DtoEncoder


@DtoEncoder
class ResponseDto:
    def __init__(self, group_list: list, category: str):
        self.status: str = "Success"
        self.data: dict = {
            category: group_list
        }
