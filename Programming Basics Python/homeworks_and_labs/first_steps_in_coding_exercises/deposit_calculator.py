deposit_amount = float(input())
deposit_term = int(input())
interest_rate = float(input())

interest = deposit_amount * (interest_rate / 100)
interest_for_month = interest / 12

total_amount = deposit_amount + deposit_term * interest_for_month

print(total_amount)