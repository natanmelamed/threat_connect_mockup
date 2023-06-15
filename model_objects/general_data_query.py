from pydantic import BaseModel


class GeneralDataQuery(BaseModel):
    scenario_mode: bool
    current_scenario: str
    max_number_of_alerts: int
    alerts_number_to_create_each_time: int
