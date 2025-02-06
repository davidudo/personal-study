"""
PROBLEM 2 - Paying Debt Off in a Year

Now write a program that calculates the minimum fixed monthly payment needed in
order pay off a credit card balance within 12 months. By a fixed monthly
payment, we mean a single number which does not change each month, but instead
is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

  1. balance - the outstanding balance on the credit card

  2. annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay
off all debt in under 1 year, for example:

```
Lowest Payment: 180
```

Assume that the interest is compounded monthly according to the balance at the
end of the month (after the payment for that month is made). The monthly
payment must be a multiple of $10 and is the same for all months. Notice that
it is possible for the balance to become negative using this payment scheme,
which is okay. A summary of the required math is found below:

  Monthly interest rate = (Annual interest rate) / 12.0
  Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
  Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

def credit_balance(balance, annual_interest_rate):
  """
  Calculates the minimum fixed monthly payment needed to pay off a credit card
  balance within 12 months.

  Args:

      balance (float): The outstanding balance on the credit card.
      annual_interest_rate (float): The annual interest rate as a decimal.

  Returns:

      int: The lowest monthly payment (multiple of $10) that pays off the
      balance in under 1 year.
  """
  num_of_months = 12
  monthly_payment = 0
  monthly_interest_rate = annual_interest_rate / num_of_months

  while True:
    remaining_balance = balance

    for _ in range(num_of_months):
      monthly_unpaid_balance = remaining_balance - monthly_payment
      remaining_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)

    if remaining_balance <= 0:
      break
    else:
      monthly_payment += 10

  return monthly_payment
