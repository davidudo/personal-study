"""
PROBLEM 1 - Paying Debt off in a Year

Write a program to calculate the credit card balance after one year if a person
only pays the minimum monthly payment required by the credit card company each
month.

The following variables contain values as described below:

  1. `balance` - the outstanding balance on the credit card

  2. `annualInterestRate` - annual interest rate as a decimal

  3. `monthlyPaymentRate` - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining
balance. At the end of 12 months, print out the remaining balance. Be sure to
print out no more than two decimal digits of accuracy - so print


```
Remaining balance: 813.41
```

instead of

```
Remaining balance: 813.4141998135
```

So your program only prints out one thing: the remaining balance at the end of
the year in the format:

```
Remaining balance: 4784.0
```

A summary of the required math is found below:

  Monthly interest rate = (Annual interest rate) / 12.0
  Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
  Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
  Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

We provide sample test cases below. We suggest you develop your code on your
own machine, and make sure your code passes the sample test cases, before you
paste it into the box below.
"""

def credit_balance_iter(balance, annual_interest_rate, monthly_payment_rate):
  """
  Calculates the remaining balance on a credit card after a specified number of
  months (mutable version).

  Args:

      balance (float): Initial balance on the credit card.

      annual_interest_rate (float): Annual interest rate as a decimal
      (e.g., 0.18 for 18%).

      monthly_payment_rate (float): Minimum monthly payment rate as a decimal
      (e.g., 0.02 for 2%).

  Returns:

      float: Remaining balance after the specified number of months, rounded to
      2 decimal places.
  """
  remaining_balance = balance
  num_of_months = 12

  for _ in range(num_of_months):
    minimum_payment = remaining_balance * monthly_payment_rate
    unpaid_balance = remaining_balance - minimum_payment
    interest = (annual_interest_rate / num_of_months) * unpaid_balance
    remaining_balance = round(unpaid_balance + interest, 2)

  return remaining_balance

def credit_balance_recur(balance, annual_interest_rate, monthly_payment_rate, num_of_months=12, current_month=0):
    """
    Calculates the remaining balance on a credit card after a specified number
    of months (immutable version).

    Args:

        balance (float): Initial balance on the credit card.

        annual_interest_rate (float): Annual interest rate as a decimal
        (e.g., 0.18 for 18%).

        monthly_payment_rate (float): Minimum monthly payment rate as a decimal
        (e.g., 0.02 for 2%).

        num_of_months (int): Number of months to simulate (default is 12).

        current_month (int): Current month in the simulation
        (used for recursion).

    Returns:

        float: Remaining balance after the specified number of months, rounded to 2 decimal places.
    """
    if current_month >= num_of_months:
        return round(balance, 2)

    minimum_payment = balance * monthly_payment_rate
    unpaid_balance = balance - minimum_payment
    interest = (annual_interest_rate / 12) * unpaid_balance
    new_balance = unpaid_balance + interest

    return credit_balance_recur(new_balance, annual_interest_rate, monthly_payment_rate, num_of_months, current_month + 1)
