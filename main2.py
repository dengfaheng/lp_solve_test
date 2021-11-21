from numpy import array
from lpsolve55 import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lp_handle = lpsolve('read_mps', "neos20.mps")
    lpsolve('solve', lp_handle)
    print(lpsolve('get_objective', lp_handle))
    print(lpsolve('get_variables', lp_handle)[0])
    print(lpsolve('get_constraints', lp_handle)[0])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
