import statsmodels.api as sm

x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 9, 11]

x = sm.add_constant(x)
model = sm.OLS(y, x).fit()

print(model.summary())
