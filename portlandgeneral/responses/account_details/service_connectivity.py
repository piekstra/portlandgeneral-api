

class ServiceConnectivity:

    def __init__(self, service_connectivity_json):
        self.is_eligible_for_reconnect: bool = service_connectivity_json.get('isEligibleForReconnect')
        self.is_disconnected: bool = service_connectivity_json.get('isDisconnected')
        self.is_reconnect_in_progress: bool = service_connectivity_json.get('isReconnectInProgress')

        # Value: ServiceConnectivity
        self._typename: bool = service_connectivity_json.get('_typename')
