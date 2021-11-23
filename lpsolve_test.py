# -*- coding: UTF-8 -*-

import sys
import csv
from lpsolve55 import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(sys.argv)
    if len(sys.argv) < 2:
        print("usage wrong!")
        exit(-1)
    file_name = sys.argv[1]
    print(file_name)
    lp_handle = lpsolve('read_mps', file_name)
    lpsolve('solve', lp_handle)
    print("------------------------------------------------------------------------\n")
    print("objective             = ", round(lpsolve('get_objective', lp_handle), 2))
    # print("variables             = ", lpsolve('get_variables', lp_handle)[0])
    print("number of variables   = ", lpsolve('get_Ncolumns', lp_handle))
    print("number of constraints = ", lpsolve('get_Nrows', lp_handle))
    print("number of nonzeros    = ", lpsolve('get_nonzeros', lp_handle))
    print("time elapsed          = ", round(lpsolve('time_elapsed', lp_handle), 4))
    print("------------------------------------------------------------------------\n")
    # 写入文件
    f = open('lpsolve_summary.csv', 'a+', encoding='utf-8', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow([file_name, lpsolve('get_Ncolumns', lp_handle),
                         lpsolve('get_Nrows', lp_handle), lpsolve('get_nonzeros', lp_handle),
                         round(lpsolve('get_objective', lp_handle), 2), round(lpsolve('time_elapsed', lp_handle), 4)])
    f.close()
