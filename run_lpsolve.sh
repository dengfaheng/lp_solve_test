dir=MPS_Files

for file in $dir/*; do
    python lpsolve_test.py $file
done
