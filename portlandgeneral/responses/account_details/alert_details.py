from typing import List

from .alert import Alert


class AlertDetails:

    def __init__(self, alert_details_json: dict):

        self.phone_number: str = alert_details_json.get('phoneNumber')
        self.phone_sequence: int = alert_details_json.get('phoneSequence')
        self.not_enrolled: bool = alert_details_json.get('notEnrolled')
        self.alerts: List[Alert] = [Alert(j) for j in alert_details_json.get('alerts')]

        # Value: AlertDetails
        self.__typename: str = alert_details_json.get('__typename')
