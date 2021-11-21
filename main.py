from numpy import array
from lpsolve55 import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lp = lpsolve('make_lp', 0, 4)
    lpsolve('set_verbose', lp, IMPORTANT)
    lpsolve('set_obj_fn', lp, [1, 3, 6.24, 0.1])
    lpsolve('add_constraint', lp, [0, 78.26, 0, 2.9], GE, 92.3)
    lpsolve('add_constraint', lp, [0.24, 0, 11.31, 0], LE, 14.8)
    lpsolve('add_constraint', lp, [12.68, 0, 0.08, 0.9], GE, 4)
    lpsolve('set_lowbo', lp, 1, 28.6)
    lpsolve('set_lowbo', lp, 4, 18)
    lpsolve('set_upbo', lp, 4, 48.98)
    lpsolve('set_col_name', lp, 1, 'COLONE')
    lpsolve('set_col_name', lp, 2, 'COLTWO')
    lpsolve('set_col_name', lp, 3, 'COLTHREE')
    lpsolve('set_col_name', lp, 4, 'COLFOUR')
    lpsolve('set_row_name', lp, 1, 'THISROW')
    lpsolve('set_row_name', lp, 2, 'THATROW')
    lpsolve('set_row_name', lp, 3, 'LASTROW')
    lpsolve('write_lp', lp, 'a.lp')
    print(lpsolve('get_mat', lp, 1, 2))
    lpsolve('solve', lp)
    print(lpsolve('get_objective', lp))
    print(lpsolve('get_variables', lp)[0])
    print(lpsolve('get_constraints', lp)[0])
    lpsolve('delete_lp', lp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
