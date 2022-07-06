

class RenewableEnrollment:

    def __init__(self, renewable_enrollment_json: dict):
        # Example: NotEnrolled
        self.renewable_enrollment_status = renewable_enrollment_json.get('renewableEnrollmentStatus')

        # Value: RenewableEnrollment
        self.__typename = renewable_enrollment_json.get('__typename')
