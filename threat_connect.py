from typing import List
from fastapi import APIRouter, Query
from threat_connect_resources import create_new_alerts, \
    _response_data_handler, get_indicator_group_details_by_category, \
    get_alert_list_by_date_added, get_alert_content_from_data_file
from model_objects.general_data_query import GeneralDataQuery
from common.data_files_handler import change_entities_number_to_create_each_request, \
    GENERAL_DATA_FILE_NAME, load_data_from_json_file_by_file_name, SCENARIO_CONFIG_FILE_NAME, \
    SCENARIO_CONFIG_FOLDER_NAME
from common.time_generator import get_current_unix_time_double_thousand, convert_timestamp_to_date
from datetime import datetime


router: APIRouter = APIRouter()


@router.get('/groups/incidents')
async def get_new_alerts(owner: str, filters: str, resultLimit: int, resultStart: int,
                            createActivityLog: bool, includes: List[str] = Query(None)) -> dict:
    return create_new_alerts(owner, filters, resultLimit,
                             resultStart, createActivityLog, includes)


@router.get('/types/indicatorTypes')
async def indicator_types() -> dict:
    return _response_data_handler.get_responses_data_by_file_name(indicator_types.__name__)


@router.post("/change_creation_size")
async def change_entities_number_to_create(general_data_query: GeneralDataQuery) -> dict:
    return change_entities_number_to_create_each_request(dict(general_data_query))


@router.get("/get_creation_size")
async def get_entities_number_to_create() -> dict:
    return load_data_from_json_file_by_file_name(GENERAL_DATA_FILE_NAME)


@router.get('/groups/threats/{incident_id}/{category}')
@router.get('/groups/incidents/{incident_id}/{category}')
async def indicator_group_details_by_category(incident_id: str, category: str) -> dict:
    return get_indicator_group_details_by_category(incident_id, category)


@router.get('/get_current_unix_time')
def get_current_unix_time() -> str:
    return str(get_current_unix_time_double_thousand())


@router.get('/get_alert_list/{unix_time}')
def get_alert_list(unix_time: int) -> list:
    found_date: datetime = convert_timestamp_to_date(unix_time)
    return get_alert_list_by_date_added(found_date)


@router.get('/get_cdc_alert/{source_id}')
def get_cdc_alert(source_id: str) -> dict:
    return get_alert_content_from_data_file(source_id, key_of_alert_id="sourceId")


@router.get('/get_complete_alert/{source_id}')
def get_complete_alert(source_id: str) -> dict:
    return get_alert_content_from_data_file(source_id, key_of_alert_id="id")


@router.get("/get_scenario_config")
async def get_scenario_configuration() -> dict:
    return load_data_from_json_file_by_file_name(SCENARIO_CONFIG_FILE_NAME, SCENARIO_CONFIG_FOLDER_NAME)
