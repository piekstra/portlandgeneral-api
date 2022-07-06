from ..responses.energy_tracker import EnergyTrackerData
from ..responses.energy_tracker import PgeEnergyTrackerData


class EnergyTracker:

    def __init__(self, encrypted_account_number: str, encrypted_person_id: str):
        self.encrypted_account_number = encrypted_account_number
        self.encrypted_person_id = encrypted_person_id
        self.base_variables = {
            'variables': {
                'params': {
                    'encryptedAccountNumber': f'{self.encrypted_account_number}',
                    'encryptedPersonId': f'{self.encrypted_person_id}'
                }
            }
        }
        self.pge_operation_name = 'getPgeEnergyTrackerData'
        self.pge_base_query_payload = {
            **self.base_variables,
            'operationName': self.pge_operation_name,
        }
        self.operation_name = 'getEnergyTrackerData'
        self.base_query_payload = {
            **self.base_variables,
            'operationName': self.operation_name,
        }

    def build_response(self, response_json: dict) -> EnergyTrackerData:
        data = response_json.get('data')
        tracker_data = data.get(self.operation_name)
        return EnergyTrackerData(tracker_data)

    def build_response_pge(self, response_json: dict) -> PgeEnergyTrackerData:
        data = response_json.get('data')
        tracker_data = data.get(self.pge_operation_name)
        return PgeEnergyTrackerData(tracker_data)

    def pge_billable_details_query(self) -> dict: return {
        **self.pge_base_query_payload,
        'query': """
query getPgeEnergyTrackerData($params: PgeEnergyTrackerDataParams) {
  getPgeEnergyTrackerData(params: $params) {
    showEnergyTracker
    serviceProvider
    identifiers
    billableAccountDetails {
      isAccountBillable
      isServiceDesignationElectric
      isAccountOnFlexPricePlan
      isNonSpo
      __typename
    }
    __typename
  }
}
"""
    }

    def data_details_query(self) -> dict: return {
        **self.base_query_payload,
        'query': """
query getEnergyTrackerData($params: EnergyTrackerDataParams) {
  getEnergyTrackerData(params: $params) {
    detailsAvailable
    showEnergyTracker
    hasMoreThan15DaysOfData
    serviceProvider
    encryptedIdentifiers
    details {
      billingCycleDay
      numberOfBillingDays
      lastReadDate
      billToDateAmount
      projectedAmount
      minProjectedAmount
      maxProjectedAmount
      billingProgress
      __typename
    }
    __typename
  }
}

"""
    }
