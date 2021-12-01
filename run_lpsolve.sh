dir=MPS_Files

for file in $dir/*; do
    python lpsolve_run.py $file
done
