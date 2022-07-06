

class PendingDisconnectStatus:

    def __init__(self, pending_disconnect_json: dict):
        self.is_pending_disconnect: bool = pending_disconnect_json.get('isPendingDisconnect')

        # Value: PendingDisconnectStatus
        self.__typename: str = pending_disconnect_json.get('__typename')
