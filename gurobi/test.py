from gurobipy import *

try:

    # Create a new model
    model = read('L1_table6.mps')

    model.optimize()

    print('Obj: ', model.objVal)

except GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')
