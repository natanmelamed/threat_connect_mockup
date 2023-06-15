from typing import Union
from fastapi.responses import JSONResponse
from error_responses import ErrorResponses
from options import TIME_FORMAT
from common.response_data_handler import ResponseDataHandler
from common.data_files_handler import load_data_from_json_file_by_file_name, \
    update_the_data_files_with_new_entities
from common import data_generator
from dto.alert_dto import AlertDto
from dto.cdc_alert_dto import CDCAlertDto
from dto.response_dto import ResponseDto
from datetime import datetime

_response_data_handler: ResponseDataHandler = ResponseDataHandler(mongo=True,
                                                                  collection_name='threat_connect')


ALERTS_DATA_FILE_NAME: str = "alerts_data.json"
CDC_ALERTS_DATA_FILE_NAME: str = "cdc_alerts_data.json"
TC_GENERAL_DATA_FILE_NAME: str = "general_data.json"


def create_new_alerts(owner: str, filters: str, resultLimit: int, resultStart: int,
                            createActivityLog: bool, includes: list) -> ResponseDto:
    alert_list_in_data_file: list = load_data_from_json_file_by_file_name(ALERTS_DATA_FILE_NAME)
    alert_cdc_list_in_data_file: list = load_data_from_json_file_by_file_name(CDC_ALERTS_DATA_FILE_NAME)
    general_data_configuration: dict = load_data_from_json_file_by_file_name(TC_GENERAL_DATA_FILE_NAME)
    alert_number_to_create_each_time: int = general_data_configuration["alerts_number_to_create_each_time"]
    alert_list: list = list()
    for index in range(0, alert_number_to_create_each_time):
        alert_id: int = int(data_generator.random_digits_string(7))
        current_alert: AlertDto = AlertDto(alert_id)
        alert_list_in_data_file.append(current_alert)
        cdc_current_alert: CDCAlertDto = CDCAlertDto(dict(current_alert))
        alert_cdc_list_in_data_file.append(cdc_current_alert)
        alert_list.append(current_alert)
    update_the_data_files_with_new_entities({ALERTS_DATA_FILE_NAME: alert_list_in_data_file,
                                             CDC_ALERTS_DATA_FILE_NAME: alert_cdc_list_in_data_file},
                                            general_data_configuration, "alerts")
    return ResponseDto(alert_list, "incident")


def get_indicator_group_details_by_category(incident_id: int, category: str) -> ResponseDto:
    group_list: list = list()
    alert_list: list = load_data_from_json_file_by_file_name(ALERTS_DATA_FILE_NAME)
    for current_alert in alert_list:
        if current_alert["id"] == incident_id:
            if category == "attributes":
                group_list: list = current_alert["attribute"]
            else:
                group_list: list = current_alert[f"associated_{category}"]
    return ResponseDto(group_list, category[:-1])


def get_alert_list_by_date_added(found_date: datetime) -> list:
    alert_list_in_the_time_frame: list = list()
    alert_list: list = load_data_from_json_file_by_file_name(ALERTS_DATA_FILE_NAME)
    for current_alert in alert_list:
        if found_date < datetime.strptime(str(current_alert["dateAdded"]).split(".")[0], TIME_FORMAT):
            alert_list_in_the_time_frame.append(current_alert["id"])

    return alert_list_in_the_time_frame


def get_alert_content_from_data_file(alert_id: str, key_of_alert_id: str) -> Union[dict, JSONResponse]:
    data_files_map: dict = {"id": ALERTS_DATA_FILE_NAME, "sourceId": CDC_ALERTS_DATA_FILE_NAME}
    alert_list: list = load_data_from_json_file_by_file_name(data_files_map[key_of_alert_id])
    for current_alert in alert_list:
        if current_alert[key_of_alert_id] == alert_id:
            return current_alert
    return ErrorResponses.get_not_found_error()
