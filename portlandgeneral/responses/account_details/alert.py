
class Alert:

    def __init__(self, alert_json: dict):

        self.description: str = alert_json.get('description')

        # Examples:
        #   Type - Description
        #   WEBUSE - Weekly Electricity Use
        #   WEBDISC - Disconnect Notice
        #   WEBEXC - Bill May Exceed
        #   WEBPYREM - Payment Reminder
        #   WEBPDA - Past Due Alert
        #   WEBPYRCV - Payment Received
        #   OUT - Outage notifications
        self.type: str = alert_json.get('type')
        self.sequence: int = alert_json.get('sequence')

        # TODO: determine type
        self.original_value = alert_json.get('originalValue')
        self.value: str = alert_json.get('value')

        self.is_email: bool = alert_json.get('isEmail')

        # TODO: determine type
        self.encrypted_email_pref_id = alert_json.get('encryptedEmailPrefId')
        self.encrypted_email_contact_id: str = alert_json.get('encryptedEmailContactId')

        self.is_text: bool = alert_json.get('isText')

        # TODO: determine type
        self.encrypted_text_pref_id = alert_json.get('encryptedTextPrefId')
        self.encrypted_text_contact_id: str = alert_json.get('encryptedTextContactId')

        # Value: Alert
        self.__typename: str = alert_json.get('__typename')
