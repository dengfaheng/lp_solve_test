# -*- coding: UTF-8 -*-

import sys
import csv
import time
from cylp.cy import CyClpSimplex

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(sys.argv)
    if len(sys.argv) < 2:
        print("usage wrong!")
        exit(-1)
    file_name = sys.argv[1]
    print(file_name)
    time_start = time.time()
    s = CyClpSimplex()
    s.readMps(file_name)
    s.initialSolve()
    time_end = time.time()
    print("------------------------------------------------------------------------\n")
    print("objective             = ", round(s.objectiveValue, 2))
    print("time elapsed          = ",  round(time_end-time_start, 4))
    print("------------------------------------------------------------------------\n")
    # 写入文件
    f = open('clp_summary.csv', 'a+', encoding='utf-8', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow([file_name, round(s.objectiveValue, 2), round(time_end-time_start, 4)])
    f.close()
