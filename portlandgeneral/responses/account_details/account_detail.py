from typing import List

from .service_address import ServiceAddress
from .bill_info import BillInfo
from .auto_pay_info import AutoPayInfo
from .payment_eligibility import PaymentEligibility
from .preferred_due_date_details import PreferredDueDateDetails
from .is_paperless_bill_enrollment_response import IsPaperlessBillEnrolledResponse
from .payment_type_plan_response import PaymentPlanTypeResponse
from .pending_disconnect_status import PendingDisconnectStatus
from .service_connectivity import ServiceConnectivity
from .alert_details import AlertDetails
from .peak_time_rebate_program_status import PeakTimeRebateProgramStatus
from .renewable_enrollment import RenewableEnrollment
from .time_of_day_info import TimeOfDayInfo
from .current_charges import CurrentCharges
from .next_bill_info import NextBillInfo
from .tpa_account_detail import TpaAccountDetail


class AccountDetail:

    def __init__(self, account_detail_json: dict):
        self.is_default: bool = account_detail_json.get('isDefault')

        # Seems to always be an int, but it comes across as a string
        self.account_number: str = account_detail_json.get('accountNumber')
        self.encrypted_account_number: str = account_detail_json.get('encryptedAccountNumber')
        self.encrypted_person_id: str = account_detail_json.get('encryptedPersonId')
        self.description: str = account_detail_json.get('description')

        # Last, First Middle Initial
        self.main_customer_name: str = account_detail_json.get('mainCustomerName')
        self.is_active: bool = account_detail_json.get('isActive')

        # Options discovered so far include: [RES, ]
        # Likely RES - Residential
        self.account_type: str = account_detail_json.get('accountType')
        self.relation_type: str = account_detail_json.get('relationType')

        # TODO: probably a list?
        self.co_customer_names = account_detail_json.get('coCustomerNames')
        self.is_logged_in_user_on_account = account_detail_json.get('isLoggedInUserOnAccount')

        self.service_addresses: List[ServiceAddress] = [ServiceAddress(j) for j in account_detail_json.get('serviceAddresses')]
        self.bill_info: BillInfo = account_detail_json.get('billInfo')
        self.auto_pay: AutoPayInfo = account_detail_json.get('autoPay')
        self.payment_eligibility: PaymentEligibility = account_detail_json.get('paymentEligibility')
        self.preferred_due_date: PreferredDueDateDetails = account_detail_json.get('preferredDueDate')
        self.is_paperless_bill_enrolled: IsPaperlessBillEnrolledResponse = account_detail_json.get('isPaperlessBillEnrolled')
        self.equal_pay: PaymentPlanTypeResponse = account_detail_json.get('equalPay')
        self.pending_disconnect: PendingDisconnectStatus = account_detail_json.get('pendingDisconnect')
        self.service_connectivity: ServiceConnectivity = ServiceConnectivity(account_detail_json.get('serviceConnectivity'))
        self.alert_details: AlertDetails = AlertDetails(account_detail_json.get('alertDetails'))
        self.peak_time_rebate: PeakTimeRebateProgramStatus = PeakTimeRebateProgramStatus(
            account_detail_json.get('peaktimeRebate'))
        self.renewable_enrollment: RenewableEnrollment = RenewableEnrollment(account_detail_json.get('renewableEnrollment'))
        self.time_of_day_info: TimeOfDayInfo = TimeOfDayInfo(account_detail_json.get('timeOfDayInfo'))
        self.current_charges: CurrentCharges = CurrentCharges(account_detail_json.get('currentCharges'))
        self.next_bill: NextBillInfo = NextBillInfo(account_detail_json.get('nextBill'))
        self.mailing_address: ServiceAddress = ServiceAddress(account_detail_json.get('mailingAddress'))
        self.tpa: TpaAccountDetail = TpaAccountDetail(account_detail_json.get('tpa'))

        # Value: AccountDetail
        self.__typename: str = account_detail_json.get('__typename')
