import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', '--first_parameter',
                    choices=['annuity', 'diff'],
                    help='indicates the type of payment: "annuity" or "diff"')
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)
args = parser.parse_args()
interest = args.interest
type_payment = args.type
principal = args.principal
periods = args.periods
payment = args.payment
if interest is None or type_payment != "annuity" and type_payment != "diff":
    print("Incorrect parameters.")
    quit()
i = interest / (12 * 100)
overpayment = 0
if type_payment == "diff" and payment is not None \
        or type_payment == "annuity" and payment is None and (periods is None and principal is None) \
        or type_payment == "diff" and (principal is None or periods is None):
    print("Incorrect parameters.")
elif type_payment == "diff":
    for m in range(1, periods + 1):
        diff = math.ceil(principal / periods + i * (principal - (principal * (m - 1)) / periods))
        print(f"Month {m}: payment is {diff}")
        overpayment += diff
    overpayment -= principal
    print(f"\nOverpayment = {overpayment}")
elif type_payment == "annuity":
    if payment is not None and periods is not None:
        principal = math.floor(payment / (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1)))
        overpayment = payment * periods - principal
        print(f"Your loan principal = {principal}!")
        print(f"Overpayment = {overpayment}")
    elif principal is not None and periods is not None:
        payment = math.ceil(principal * i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1))
        overpayment = payment * periods - principal
        print(f"Your annuity payment = {payment}!")
        print(f"Overpayment = {overpayment}")
    elif principal is not None and payment is not None:  # and interest is not None
        base = payment / (payment - i * principal)
        periods = math.ceil(math.log(base, 1 + i))
        years = periods // 12
        month = periods % 12
        if periods == 12:
            print("It will take 1 year to repay this loan!")
        elif periods == 1:
            print("It will take 1 months to repay this loan!")
        elif periods < 12:
            print(f"It will take {month} months to repay this loan!")
        elif periods > 12 and month == 0:
            print(f"It will take {years} years to repay this loan!")
        elif periods > 12 and month == 1:
            print(f"It will take {years} years and 1 month to repay this loan!")
        else:
            print(f"It will take {years} years and {month} months to repay this loan!")
        overpayment = periods * payment - principal
        print(f"Overpayment = {overpayment}")

