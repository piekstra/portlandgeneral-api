from typing import List

from ..responses.account_details import AccountDetail


class AccountDetails:

    def __init__(self, account_number: str, encrypted_person_id: str):
        self.account_number = account_number
        self.encrypted_person_id = encrypted_person_id
        self.operation_name = 'getAccountDetails'
        self.base_query_payload = {
            'operationName': self.operation_name,
            'variables': {
                'params': {
                    'accountNumberList': [
                        {
                            'accountNumber': f'{self.account_number}',
                            'encryptedPersonId': f'{self.encrypted_person_id}'
                        }
                    ]
                }
            }
        }

    def build_response(self, response_json) -> List[AccountDetail]:
        data = response_json.get('data')
        details = data.get(self.operation_name)
        return [AccountDetail(detail) for detail in details]

    def full_details_query(self) -> dict: return {
        **self.base_query_payload,
        # Extend base variables
        'variables': {
            **self.base_query_payload['variables'],
            'isTPAFeatureEnabled': True,
        },
        'query': """
query getAccountDetails($params: AccountDetailParams!, $isTPAFeatureEnabled: Boolean!) {
  getAccountDetails(params: $params) {
    accountNumber
    encryptedAccountNumber
    encryptedPersonId
    description
    accountType
    relationType
    mainCustomerName
    coCustomerNames
    isLoggedInUserOnAccount
    isDefault
    isActive
    mailingAddress {
      addressLine1
      addressLine2
      city
      state
      postal
      __typename
    }
    serviceAddresses {
      addressLine1
      addressLine2
      city
      state
      postal
      __typename
    }
    serviceConnectivity {
      isEligibleForReconnect
      isDisconnected
      isReconnectInProgress
      __typename
    }
    currentCharges {
      amountDue
      __typename
    }
    nextBill {
      billDate
      __typename
    }
    billInfo {
      amountDue
      dueDate
      lastPaymentDate
      lastPaymentAmount
      isAccountPayable
      isNewAccount
      oneTimeFuturePaymentScheduled
      multipleFuturePaymentsScheduled
      enrolledInTPA
      billDetails {
        encryptedBillId
        downloadBillUrl
        billStatus
        billDate
        dueDate
        amountDue
        previousBalance
        totalAdjustments
        totalCurrentCharges
        totalBalanceAfterBill
        hasBills
        kwh
        billingPeriodStartDate
        billingPeriodEndDate
        __typename
      }
      __typename
    }
    autoPay {
      isEnrolled
      __typename
    }
    paymentEligibility {
      isCashOnly
      isNonBillableNoBalance
      __typename
    }
    preferredDueDate {
      dueDate {
        preferredDueDate
        status
        effectiveDate
        __typename
      }
      __typename
    }
    isPaperlessBillEnrolled {
      result
      __typename
    }
    equalpay {
      paymentPlanType
      __typename
    }
    pendingDisconnect {
      isPendingDisconnect
      __typename
    }
    alertDetails {
      phoneNumber
      phoneSequence
      notEnrolled
      alerts {
        description
        type
        sequence
        originalValue
        value
        isEmail
        encryptedEmailPrefId
        encryptedEmailContactId
        isText
        encryptedTextPrefId
        encryptedTextContactId
        __typename
      }
      __typename
    }
    peaktimeRebate {
      hasActiveSA
      peakTimeRebateEnrollmentStatus
      hasRebates
      __typename
    }
    renewableEnrollment {
      renewableEnrollmentStatus
      __typename
    }
    timeOfDayInfo {
      enrollmentStatus
      __typename
    }
    tpa @include(if: $isTPAFeatureEnabled) {
      isEligible
      isEnrolled
      accountBalance
      recommendedPaymentMonths
      enrolledInstallmentDetails {
        payOffAmount
        currentTpaMonthBalance
        totalMonths
        monthsMatrix {
          monthNumber
          isPaymentCompleted
          paymentDate
          monthlyAmount
          doesBillExist
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}
"""
    }

    def dropdown_info_query(self) -> dict: return {
        **self.base_query_payload,
        'query': """
query getAccountDetails($params: AccountDetailParams!) {
  getAccountDetails(params: $params) {
    ...DropdownInfo
    __typename
  }
}

fragment DropdownInfo on AccountDetail {
  isDefault
  accountNumber
  encryptedAccountNumber
  encryptedPersonId
  description
  mainCustomerName
  isActive
  serviceAddresses {
    addressLine1
    addressLine2
    city
    state
    postal
    __typename
  }
  serviceConnectivity {
    isEligibleForReconnect
    isDisconnected
    isReconnectInProgress
    __typename
  }
  __typename
}
"""
    }

    def bill_info_query(self) -> dict: return {
        **self.base_query_payload,
        'query': """
query getAccountDetails($params: AccountDetailParams!) {
  getAccountDetails(params: $params) {
    accountNumber
    encryptedAccountNumber
    encryptedPersonId
    description
    isDefault
    isActive
    accountType
    relationType
    mainCustomerName
    coCustomerNames
    isLoggedInUserOnAccount
    serviceAddresses {
      addressLine1
      addressLine2
      city
      state
      postal
      __typename
    }
    billInfo {
      amountDue
      dueDate
      lastPaymentDate
      lastPaymentAmount
      isAccountPayable
      isNewAccount
      oneTimeFuturePaymentScheduled
      multipleFuturePaymentsScheduled
      enrolledInTPA
      billDetails {
        encryptedBillId
        downloadBillUrl
        billStatus
        billDate
        dueDate
        amountDue
        previousBalance
        totalAdjustments
        totalCurrentCharges
        totalBalanceAfterBill
        hasBills
        kwh
        billingPeriodStartDate
        billingPeriodEndDate
        __typename
      }
      __typename
    }
    autoPay {
      isEnrolled
      __typename
    }
    paymentEligibility {
      isCashOnly
      isNonBillableNoBalance
      __typename
    }
    preferredDueDate {
      dueDate {
        preferredDueDate
        status
        effectiveDate
        __typename
      }
      __typename
    }
    isPaperlessBillEnrolled {
      result
      __typename
    }
    equalpay {
      paymentPlanType
      __typename
    }
    pendingDisconnect {
      isPendingDisconnect
      __typename
    }
    serviceConnectivity {
      isEligibleForReconnect
      isDisconnected
      isReconnectInProgress
      __typename
    }
    __typename
  }
}
"""
    }

    def alert_details_query(self) -> dict: return {
        **self.base_query_payload,
        'query': """
query getAccountDetails($params: AccountDetailParams!) {
  getAccountDetails(params: $params) {
    accountNumber
    alertDetails {
      phoneNumber
      phoneSequence
      notEnrolled
      alerts {
        description
        type
        sequence
        originalValue
        value
        isEmail
        encryptedEmailPrefId
        encryptedEmailContactId
        isText
        encryptedTextPrefId
        encryptedTextContactId
        __typename
      }
      __typename
    }
    peaktimeRebate {
      hasActiveSA
      peakTimeRebateEnrollmentStatus
      hasRebates
      __typename
    }
    renewableEnrollment {
      renewableEnrollmentStatus
      __typename
    }
    timeOfDayInfo {
      enrollmentStatus
      __typename
    }
    __typename
  }
}
"""
    }

    def tpa_info_query(self) -> dict: return {
        **self.base_query_payload,
        # Extend base variables
        'variables': {
            **self.base_query_payload['variables'],
            'isTPAFeatureEnabled': True,
        },
        'query': """
query getAccountDetails($params: AccountDetailParams!, $isTPAFeatureEnabled: Boolean!) {
  getAccountDetails(params: $params) {
    currentCharges {
      amountDue
      __typename
    }
    nextBill {
      billDate
      __typename
    }
    mailingAddress {
      addressLine1
      addressLine2
      city
      state
      postal
      __typename
    }
    serviceAddresses {
      addressLine1
      addressLine2
      city
      state
      postal
      __typename
    }
    tpa @include(if: $isTPAFeatureEnabled) {
      isEligible
      isEnrolled
      accountBalance
      recommendedPaymentMonths
      enrolledInstallmentDetails {
        payOffAmount
        currentTpaMonthBalance
        totalMonths
        monthsMatrix {
          monthNumber
          isPaymentCompleted
          paymentDate
          monthlyAmount
          doesBillExist
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}
"""
    }
