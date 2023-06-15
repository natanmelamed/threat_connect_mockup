from datetime import datetime, timedelta
from common.dto_decoder import DtoEncoder
from dto.attribute_dto import AttributeDto
from dto.tag_dto import TagDto
from dto.security_lable_dto import SecurityLabelDto
from dto.associated_group_dto import AssociatedGroupDto
from dto.associated_indicator_dto import AssociatedIndicatorDto
from common.data_generator import get_random_value_list, random_int_in_range
import options


@DtoEncoder
class AlertDto:
    def __init__(self, alert_id: int):
        self.id: str = str(alert_id)
        self.name: str = f"Mock alert {alert_id} with: 1!@#$%^&*()_+=/*?><:'[]''.`~'"
        self.ownerName: str = "CyberProof"
        self.dateAdded: str = str((datetime.now() + timedelta(seconds=3)).strftime(options.TIME_FORMAT))
        self.webLink: str = f"https://testowner.tc.com/auth/incident/incident.xhtml?incident={alert_id}"
        self.attribute: list = get_random_value_list(random_int_in_range(1, 3), AttributeDto,
                                                     return_fixed_no_of_values=True)
        self.tag: list = get_random_value_list(random_int_in_range(2, 4), TagDto,
                                               return_fixed_no_of_values=True)
        self.xid: str = f"f73e684c-11b2-4c38-a29a-8eb759b25c5b:{alert_id}"
        self.securityLabel: list = get_random_value_list(random_int_in_range(2, 4), SecurityLabelDto,
                                                         return_fixed_no_of_values=True)
        self.eventDate: str = str((datetime.now() + timedelta(seconds=3)).strftime(options.TIME_FORMAT))
        self.status: str = "Incident Reported"
        self.associated_groups: list = get_random_value_list(random_int_in_range(2, 4), AssociatedGroupDto,
                                                             return_fixed_no_of_values=True)
        self.associated_indicators: list = get_random_value_list(random_int_in_range(2, 4), AssociatedIndicatorDto,
                                                                 return_fixed_no_of_values=True)
        mandatory_attribute: AttributeDto = AttributeDto()
        mandatory_attribute["type"]: str = "Source"
        mandatory_attribute["value"]: str = "Sample URL"
        self.attribute.append(mandatory_attribute)

        mandatory_attribute: AttributeDto = AttributeDto()
        mandatory_attribute["type"]: str = "Description"
        mandatory_attribute["value"]: str = "Mock description new incident, new modification"
        self.attribute.append(mandatory_attribute)

        mandatory_attribute: AttributeDto = AttributeDto()
        mandatory_attribute["type"]: str = "TCC"
        mandatory_attribute["value"]: str = "TCC-123456"
        self.attribute.append(mandatory_attribute)

