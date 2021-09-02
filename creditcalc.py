import math
import argparse


def loan_principal():
    i = args.interest / (12 * 100)
    p = args.payment / ((i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1))
    print(f'Your loan principal = {round(p)}!')


def number_of_monthly_payments():
    i = args.interest / (12 * 100)
    n = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
    if n > 11 and n % 12 != 0:
        print(f'It will take {n // 12} years and {n - n // 12 * 12} months to repay the loan!')
    if n > 11 and n % 12 == 0:
        print(f'It will take {n // 12} years to repay the loan!')
    else:
        if 1 < n < 12:
            print(f'It will take {n} months to repay the loan!')
        else:
            print(f'It will take {n} month to repay the loan!')
    print(f'Overpayment = {n * args.payment - args.principal}')


def annuity_payment():
    i = args.interest / (12 * 100)
    a = args.principal * ((i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1))
    print(f'Your monthly payment = {math.ceil(a)}!')


def differentiated_payment():
    i = args.interest / (12 * 100)
    m = 1
    op = 0

    while m <= args.periods:
        a = math.ceil(
            args.principal / args.periods + i * (args.principal - ((args.principal * (m - 1)) / args.periods)))
        op += a
        print(f'Month {m}: payment is {a}')
        m += 1

    print(f'\nOverpayment = {round(op - args.principal)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', choices=['diff', 'annuity'])
    parser.add_argument('--principal', type=float)
    parser.add_argument('--periods', type=float)
    parser.add_argument('--interest', type=float)
    parser.add_argument('--payment', type=int)
    args = parser.parse_args()

    if args.type == 'diff':
        if args.type and args.principal and args.periods and args.interest:
            differentiated_payment()
        else:
            print('Incorrect parameters')
    elif args.type == 'annuity':
        if args.type and args.principal and args.periods and args.interest:
            annuity_payment()
        elif args.type and args.payment and args.periods and args.interest:
            loan_principal()
        elif args.type and args.principal and args.payment and args.interest:
            number_of_monthly_payments()
        else:
            print('Incorrect parameters')
