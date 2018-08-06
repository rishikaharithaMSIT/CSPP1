'''
Author: Rishika Haritha - 20186041
Encoding: Utf-8
'''

def payingDebtOffInAYear(balance_unpaid, annual_interest_rate, monthly_payment_rate):
    '''to calculate remaining balance'''
    balance_copy = balance_unpaid

    iterator_i = 1
    while iterator_i <= 12:
        montly_interest_rate = annual_interest_rate / 12.0
        minimum_monthly_payment = monthly_payment_rate*balance_copy
        monthly_unpaid_balance = balance_copy - minimum_monthly_payment
        balance_copy = monthly_unpaid_balance + (montly_interest_rate * monthly_unpaid_balance)
        iterator_i += 1
    return "Remaining balance: "+str(round(balance_copy, 2))
    

def main():
    '''main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(payingDebtOffInAYear(data[0],data[1],data[2]))

if __name__ == "__main__":
    main()

