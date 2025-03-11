from scipy.optimize import minimize
#  This is a script to determine how much of 100k should be invested in two projects to maximize the return.

#Return of the projects is 20% + the root of money invested for the first one and 10% for the second
def objfunc(x):
    x1 = x[0]
    x2 = x[1]

    return -(1.2*x1 + x1 ** 0.5 + 1.1*x2)

#Trivial condition of the sum of the investments cannot exceed 100k
def c1(x):
    return 100 - x[0] - x[1]

#The risk is given by this equation and cannot exceed half of the 100k
def c2(x):
    return 50 - x[0] - x[1]**0.7

#set the constraints as a dict with two funcs
constraints = (
    {'type': 'ineq', 'fun': c1 },
    {'type': 'ineq', 'fun': c2}
)
#Bounds, for x1 is 0 and no upper limit, for x2 is 0 and 20k as the maximum
bounds = ((0, None), (0, 20))
#Initial guess
x0 = (1, 10)

res = minimize(objfunc, x0, bounds=bounds, constraints=constraints, options={'disp':True})

print(f"First project: {res.x[0]:.3f}k")
print(f"Second project:{res.x[1]:.3f}k")