from common import common_options
from common.dto_decoder import DtoEncoder
from common.json_parser import get_first_property_from_json_content


@DtoEncoder
class CDCAlertDto:
    def __init__(self, alert_dto: dict):
        severity_map: list = [
            attr["value"]
            for attr in alert_dto["attribute"]
            if attr["type"] == "Threat Level"
        ]
        severity: str = severity_map[0] if len(severity_map) > 0 else "Medium"

        description: list = [
            attr["value"]
            for attr in alert_dto["attribute"]
            if attr["type"] == "Description"
        ]
        self.description: str = description[0][:2000] if len(description) > 0 else ""

        self.source: str = "CTI"
        self.name: str = "CTI - " + get_first_property_from_json_content("name", alert_dto)
        self.sourceId: str = get_first_property_from_json_content("id", alert_dto)
        self.sourceUrl: str = get_first_property_from_json_content("webLink", alert_dto)
        self.severity: dict = {
            "value": severity,
            "color": common_options.severity_map[severity]["color"],
            "order": common_options.severity_map[severity]["order"]
        }
