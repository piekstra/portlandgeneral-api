from .preferred_due_date import PreferredDueDate


class PreferredDueDateDetails:

    def __init__(self, preferred_due_date_json: dict):
        self.due_date: PreferredDueDate = PreferredDueDate(preferred_due_date_json.get('dueDate'))

        # Value: PreferredDueDate
        self.__typename: str = preferred_due_date_json.get('PreferredDueDateDetails')
