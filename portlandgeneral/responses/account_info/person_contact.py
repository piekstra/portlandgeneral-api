class PersonContact:

    def __init__(self, person_contact_json: dict):

        # Example: EMAIL, PNP, MOB
        self.contact_type: str = person_contact_json.get('contactType')

        # Example: example@gmail.com, "(123) 456-7890"
        self.contact_value: str = person_contact_json.get('contactValue')

        # Value: PersonContact
        self.__typename: str = person_contact_json.get('__typename')
