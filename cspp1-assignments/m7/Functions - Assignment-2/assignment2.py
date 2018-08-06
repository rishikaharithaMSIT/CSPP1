'''
Author: Rishika Haritha - 20186041
Encoding: Utf-8
'''

def paying_debt(balance_unpaid, annual_interest_rate, guess_num):
    balance_copy = balance_unpaid

    iterator_i = 1
    while i <= 12:
        montly_interest_rate = annual_interest_rate / 12      
        monthly_unpaid_balance = balance_copy - guess_num
        balance_copy = mub + (montly_interest_rate * monthly_unpaid_balance)
        iterator_i += 1
    return balance_copy

def paying_debt_off_inayear(balance_unpaid, annual_interest_rate):
    balance_copy = balance_unpaid
    aprroximation_val = 0.1
    step_val = 1
    guess_num = 0.0
    while payingDebt(balance_copy, annual_interest_rate, guess_num * 10) >= aprroximation_val:      
        guess_num += step_val         
    
    min_pay = round(guess_num)
    return "Lowest Payment: "+str(min_pay * 10)
    
def main():
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(paying_debt_off_inayear(data[0], data[1]))
    
if __name__ == "__main__":
    main()