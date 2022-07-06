

class PeakTimeRebateProgramStatus:

    def __init__(self, peak_time_rebate_json: dict):
        self.has_active_sa: bool = peak_time_rebate_json.get('hasActiveSA')

        # Example: YetToEnroll
        self.peak_time_rebate_enrollment_status: str = peak_time_rebate_json.get('peakTimeRebateEnrollmentStatus')
        self.has_rebates: bool = peak_time_rebate_json.get('hasRebates')

        # Value: PeakTimeRebateProgramStatus
        self.__typename: str = peak_time_rebate_json.get('__typename')
