"""
PROBLEM 2 - Paying Debt Off in a Year

You'll notice that in Problem 2, your monthly payment had to be a multiple of
$10. Why did we make it that way? You can try running your code locally so that
the payment can be any dollar and cent amount (in other words, the monthly
payment is a multiple of $0.01). Does your code still work? It should, but you
may notice that your code runs more slowly, especially in cases with very large
balances and interest rates. (Note: when your code is running on our servers,
there are limits on the amount of computing time each submission is allowed, so
your observations from running this experiment on the grading system might be
limited to an error message complaining about too much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment than we
did in Problem 2 without running into the problem of slow code? We can make
this program run faster using a technique introduced in lecture - bisection
search!

The following variables contain values as described below:

    1. balance - the outstanding balance on the credit card

    2. annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such
that we can pay off the entire balance within a year. What is a reasonable
lower bound for this payment value? $0 is the obvious anwer, but you can do
better than that. If there was no interest, the debt can be paid off by monthly
payments of one-twelfth of the original balance, so we must pay at least this
much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off
the entire balance at the end of the year. What we ultimately pay must be
greater than what we would've paid in monthly installments, because the
interest was compounded on the balance we didn't pay off each month. So a good
upper bound for the monthly payment would be one-twelfth of the balance, after
having its interest compounded monthly for an entire year.

In short:

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly payment lower bound = Balance / 12
    Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search (for more info
check out the Wikipedia page on bisection search) to find the smallest monthly
payment to the cent (no more multiples of $10) such that we can pay off the
debt within a year. Try it out with large inputs, and notice how fast it is
(try the same large inputs in your solution to Problem 2 to compare!). Produce
the same return value as you did in Problem 2.

Note that if you do not use bisection search, your code will not run - your
code only has 30 seconds to run on our servers.
"""

def credit_balance(balance, annual_interest_rate):
  """
    Calculate the minimum fixed monthly payment required to pay off a credit
    card balance within 12 months, using the bisection method.

    The function simulates monthly payments and adjusts the payment amount
    iteratively until the remaining balance is within a specified tolerance of
    zero.

    Parameters:

        balance (float): The initial credit card balance.

        annual_interest_rate (float): The annual interest rate (expressed as a
        decimal, e.g., 0.2 for 20%).

    Returns:

        float: The minimum fixed monthly payment required to pay off the
        balance in 12 months, rounded to 2 decimal places.

    Example:

        >>> credit_balance(320000, 0.2)
        29157.09
    """
  tolerance = 0.01
  num_of_months = 12
  monthly_interest_rate = annual_interest_rate / num_of_months

  lower = balance / num_of_months
  upper = (balance * (1 + monthly_interest_rate) ** num_of_months) / num_of_months

  while (upper - lower) > tolerance:
    remaining_balance = balance
    mid = (upper + lower) / 2

    for _ in range(num_of_months):
      monthly_unpaid_balance = remaining_balance - mid
      remaining_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)

    if remaining_balance < 0:
      upper = mid
    else:
      lower = mid

  return round((upper + lower) / 2, 2)
