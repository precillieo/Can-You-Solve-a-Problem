def roi(capital, duration, percent):
    
    """
    roi() calculates the cumulative return on investment of a certain amount for a given time at a given interest rate.
    
    parameters:
    capital: amount to be invested
    duration: how long one is investing in months
    percent: the interest rate per month
    """
    cum = [capital]
    percentage = percent/100
    for num in range(duration):
        profit = cum[-1]*percentage
        total_amt = cum[-1] + profit
        cum.append(total_amt)
    investment_yield = cum[-1]
    return investment_yield

x = int(input('Input your capital: '))
y = int(input('Input your duration: '))
z = int(input('Input your percentage: '))
invest = roi(x,y,z)
print(f'Your investment ROI on {x} after {y} months is {round(invest)}')
