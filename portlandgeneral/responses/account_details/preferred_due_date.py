

class PreferredDueDate:

    def __init__(self, due_date_json: dict):

        # Day of the month, like 16
        self.preferred_due_date: int = due_date_json.get('preferredDueDate')

        # Example: "Found"
        self.status: str = due_date_json.get('status')

        # Format: 2022-01-01T00:00:00
        self.effective_date: str = due_date_json.get('effectiveDate')

        # Value: PreferredDueDate
        self.__typename: str = due_date_json.get('__typename')
