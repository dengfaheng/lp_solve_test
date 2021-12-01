dir=MPS_Files_DIFF

for file in $dir/*; do
    python lpsolve_test_pre_solve_all.py $file
done
