from enum import Enum

class PaymentMethods(Enum):
    PAYMENT_METHOD_CASH = "cash"
    PAYMENT_METHOD_DEBIT_CARD = "debit_card"
    PAYMENT_METHOD_CREDIT_CARD = "credit_card"
    PAYMENT_METHOD_EWALLET = "ewallet"
    PAYMENT_METHOD_QRIS = "qris"
    PAYMENT_METHOD_POINT_REDEMPTION = "point_redemption"