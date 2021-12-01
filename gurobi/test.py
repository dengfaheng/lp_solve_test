from gurobipy import *

try:

    # Create a new model
    model = read('E226.mps')

    model.optimize()

    print('Obj: ', model.objVal)

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')
