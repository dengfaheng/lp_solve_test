# -*- coding: UTF-8 -*-

import sys
import csv
from lpsolve55 import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(sys.argv)
    if len(sys.argv) < 2:
        print("usage wrong!")
        # exit(-1)
    file_name = sys.argv[1]
    print(file_name)
    lp_handle = lpsolve('read_mps', file_name)
    lpsolve('write_mps', lp_handle, 'new_'+file_name)

